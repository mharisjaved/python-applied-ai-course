"""Course LLM helper: ask_llm() talks to Claude, or to a pretend model when offline.

    from llm import ask_llm
    reply = ask_llm("Classify the sentiment of this review in one word: <review>Great lamp!</review>")

ask_llm() calls the real Claude API only when ANTHROPIC_API_KEY is set (for example in a .env
file) and COURSE_OFFLINE is not "1". Otherwise it returns mock_llm(prompt).

The mock is NOT intelligent. It follows a few fixed rules, so lessons and tests give the same
answer every time:

* Which text it analyses: the text inside <review>...</review> (or <text>...</text> or triple
  quotes) if present, otherwise the text after the last "Review:", otherwise the whole prompt.
* Sentiment: counts positive and negative words. "not good" counts as negative and a review
  containing "oh great" is treated as sarcastic. It answers "mixed" or "neutral" only if the
  prompt mentions that label.
* Format: "JSON" in the prompt gives a JSON object with sentiment, topics and summary (with a
  friendly sentence and a code fence around it, unless the prompt says "only"). "one word" in
  the prompt, or a prompt ending with ":", gives just the label. Otherwise: a chatty sentence.
* Other tasks: "Question:" answers from the text (and makes something up unless the prompt
  allows "I don't know"), "draft a reply" drafts a reply to the customer, "summar..." gives the first
  sentence.
* Prompt injection: if the review is NOT inside delimiters and says "ignore previous
  instructions", the mock obeys it (real models can be fooled too).
* The system message is ignored.
"""

import json
import os

import anthropic
from dotenv import load_dotenv

load_dotenv()  # copy ANTHROPIC_API_KEY and LLM_MODEL from a .env file (if any) into os.environ
MODEL = os.environ.get("LLM_MODEL", "claude-opus-5-5")  # read AFTER load_dotenv(), so .env counts

# --------------------------------------------------------------------------------------------
# Part 1: the mock model (no internet, no key, same answer every time)
# --------------------------------------------------------------------------------------------

POSITIVE_WORDS = [
    "great", "good", "love", "perfect", "comfortable", "clear", "happy", "easy", "solid",
    "recommended", "best", "brilliant", "bright", "nice", "handy", "friendly", "strong",
    "dry", "fits", "fit", "excellent", "better", "light", "adjustable", "well", "cheaper",
]
NEGATIVE_WORDS = [
    "bad", "terrible", "poor", "broke", "broken", "cracked", "crushed", "leaks", "disconnecting",
    "stopped", "flickers", "headache", "returned", "disappointed", "ripped", "peeling", "wrong",
    "late", "droops", "loud", "cheap", "confusing", "hurt", "died", "worst", "sensitive", "short",
    "heavier", "refund", "costs",
]
NEGATION_WORDS = ["not", "never", "no"]
TOPIC_WORDS = {
    "battery": "battery", "charging": "battery",
    "sound": "sound", "noise": "sound", "microphone": "sound", "loud": "sound",
    "disconnecting": "connection", "pairing": "connection",
    "comfortable": "comfort", "blisters": "comfort", "straps": "comfort", "cushioning": "comfort",
    "knees": "comfort",
    "broke": "quality", "cracked": "quality", "ripped": "quality", "stitching": "quality",
    "peeling": "quality", "cheap": "quality", "flickers": "quality", "droops": "quality",
    "leaks": "quality", "died": "quality", "quality": "quality", "build": "quality",
    "delivery": "delivery", "delivered": "delivery", "arrived": "delivery", "box": "delivery",
    "price": "price", "cheaper": "price", "money": "price",
    "size": "size", "sizes": "size", "pockets": "size", "pocket": "size", "heavier": "size",
    "colour": "design", "design": "design", "looks": "design",
    "support": "support", "refund": "support", "return": "support", "returned": "support",
    "timer": "ease of use", "instructions": "ease of use", "button": "ease of use",
    "clean": "ease of use", "adjustable": "ease of use",
    "light": "light", "bright": "light", "grip": "grip", "laces": "fit", "fits": "fit",
    "rainy": "weather", "dry": "weather",
}
LABELS = ["positive", "negative", "mixed", "neutral"]
DELIMITERS = [("<review>", "</review>"), ("<text>", "</text>"), ('"""', '"""')]
INJECTION_PHRASES = [
    "ignore previous instructions", "ignore all previous instructions",
    "ignore the previous instructions", "ignore your instructions",
    "ignore the instructions above",
]
REPLY_PHRASES = ["draft a reply", "write a reply", "reply to this review", "reply to the customer"]
QUESTION_STOP_WORDS = ["about", "which", "where", "there", "their", "would", "could", "should",
                       "these", "those", "review", "answer", "question", "after", "before"]
PUNCTUATION = ".,!?;:()\"'"


def split_words(text):
    """Return the lowercase words of text without punctuation around them."""
    words = []
    for word in text.lower().split():
        word = word.strip(PUNCTUATION)
        if word:
            words.append(word)
    return words


def find_review_text(prompt):
    """Split the prompt into (review_text, instructions, how_found).

    how_found is "delimited" (tags or triple quotes), "labelled" (after "Review:") or "whole".
    """
    for start_tag, end_tag in DELIMITERS:
        end = prompt.rfind(end_tag)
        start = prompt.rfind(start_tag, 0, end)
        if end != -1 and start != -1:
            review = prompt[start + len(start_tag):end].strip()
            instructions = prompt[:start] + " " + prompt[end + len(end_tag):]
            return review, instructions, "delimited"
    label_index = prompt.lower().rfind("review:")
    if label_index != -1:
        label_end = label_index + len("review:")
        lines = prompt[label_end:].strip().split("\n")
        if lines[0].strip():
            instructions = prompt[:label_end] + "\n" + "\n".join(lines[1:])
            return lines[0].strip(), instructions, "labelled"
    return prompt, prompt, "whole"


def count_sentiment(text):
    """Return (positive_count, negative_count) for the words in text."""
    words = split_words(text)
    positive = 0
    negative = 0
    for index, word in enumerate(words):
        negated = index > 0 and words[index - 1] in NEGATION_WORDS
        if word in POSITIVE_WORDS and negated:
            negative += 1
        elif word in POSITIVE_WORDS:
            positive += 1
        elif word in NEGATIVE_WORDS:
            negative += 1
    if "oh great" in text.lower():  # a (very) simple sarcasm rule: the praise is not meant
        negative = negative + positive
        positive = 0
    return positive, negative


def choose_label(positive, negative, allowed):
    """Turn word counts into a label. Only uses "mixed"/"neutral" if they are allowed."""
    if positive > 0 and negative > 0 and abs(positive - negative) <= 1 and "mixed" in allowed:
        return "mixed"
    if positive > negative:
        return "positive"
    if negative > positive:
        return "negative"
    if "neutral" in allowed:
        return "neutral"
    if "mixed" in allowed:
        return "mixed"
    return "neutral"  # unsure and no rule given: like a real model, it may break your label list


def find_topics(text):
    """Return up to 3 topics mentioned in text, in order of appearance."""
    topics = []
    for word in split_words(text):
        topic = TOPIC_WORDS.get(word)
        if topic is not None and topic not in topics:
            topics.append(topic)
    return topics[:3]


def first_sentence(text, max_words=15):
    """Return the first sentence of text, shortened to max_words words."""
    sentence = text.strip()
    for mark in [". ", "! ", "? "]:
        index = sentence.find(mark)
        if index != -1:
            sentence = sentence[:index + 1]
    words = sentence.split()
    if len(words) > max_words:
        sentence = " ".join(words[:max_words]) + "..."
    return sentence


def format_answer(label, review, instructions):
    """Present a sentiment label in the format the instructions ask for."""
    if "json" in instructions:
        data = {"sentiment": label, "topics": find_topics(review), "summary": first_sentence(review)}
        text = json.dumps(data)
        if "only" in instructions:
            return text
        return "Here is the analysis you asked for:\n```json\n" + text + "\n```"
    if "one word" in instructions or instructions.rstrip().endswith(":"):
        return label
    topics = find_topics(review)
    if topics:
        return f"Sure! Overall I would say this review is {label}. It talks about {', '.join(topics)}."
    return f"Sure! Overall I would say this review is {label}."


def obey_injection(prompt, instructions):
    """Pretend to be fooled by "ignore previous instructions" (returns None if not found)."""
    lowered = prompt.lower()
    for phrase in INJECTION_PHRASES:
        index = lowered.find(phrase)
        if index != -1:
            after = lowered[index + len(phrase):]
            for label in LABELS:
                if label in after:
                    return format_answer(label, "", instructions)
            return "OK! I will ignore my previous instructions. What should I do instead?"
    return None


def answer_question(prompt, review, how_found):
    """Answer the question after "Question:" using only the given text, or make something up."""
    question_index = prompt.lower().rfind("question:")
    question = prompt[question_index + len("question:"):].strip().split("\n")[0]
    if how_found == "delimited":
        context = review
    else:
        context = prompt[:question_index]
    keywords = [word for word in split_words(question)
                if len(word) >= 5 and word not in QUESTION_STOP_WORDS]
    for keyword in keywords:
        for sentence in context.replace("!", ".").replace("?", ".").split("."):
            if keyword in sentence.lower():
                return sentence.strip() + "."
    if "don't know" in prompt.lower() or "do not know" in prompt.lower():
        return "I don't know. The text does not say."
    if keywords:  # no answer in the text, so the mock "hallucinates" a confident one
        return f"Yes, the {keywords[-1]} is included and it lasts for 2 years."
    return "Yes, definitely."


def draft_reply(review):
    """Draft a short, polite reply to a customer review."""
    positive, negative = count_sentiment(review)
    topics = find_topics(review)
    about = "product"
    if topics:
        about = " and ".join(topics)
    if positive > negative:
        return "Thank you for your kind review! We are glad you are happy with your purchase."
    if negative > positive:
        return (f"We are sorry to hear about the problem with the {about}. "
                "Please contact our support team so we can put it right.")
    return f"Thank you for your honest feedback about the {about}. We will share it with our team."


def mock_llm(prompt):
    """A pretend LLM: deterministic, keyword-based replies (see the rules at the top of the file)."""
    review, instructions, how_found = find_review_text(prompt)
    instructions = instructions.lower()
    if how_found != "delimited":
        fooled = obey_injection(prompt, instructions)
        if fooled is not None:
            return fooled
    if "question:" in instructions:
        return answer_question(prompt, review, how_found)
    if any([phrase in instructions for phrase in REPLY_PHRASES]):
        return draft_reply(review)
    task_words = ["sentiment", "review", "positive", "negative", "classify", "json"]
    if "summar" in instructions and "sentiment" not in instructions and "json" not in instructions:
        return first_sentence(review)
    if not any([word in instructions for word in task_words]):
        return ("[mock model] Offline I can only classify the sentiment of a review, summarise "
                "a text, answer a question about a text and draft a reply to a review.")
    allowed = [label for label in LABELS if label in instructions]
    positive, negative = count_sentiment(review)
    label = choose_label(positive, negative, allowed)
    return format_answer(label, review, instructions)


# --------------------------------------------------------------------------------------------
# Part 2: the real model (only used when an API key is available)
# --------------------------------------------------------------------------------------------

def ask_llm(prompt, system="You are a helpful assistant."):
    """Send one prompt to Claude and return its text reply (mock reply when offline)."""
    if os.environ.get("COURSE_OFFLINE") == "1" or not os.environ.get("ANTHROPIC_API_KEY"):
        return mock_llm(prompt)
    client = anthropic.Anthropic()  # picks up ANTHROPIC_API_KEY automatically
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=system,
        messages=[{"role": "user", "content": prompt}],
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",  # if this model declines, the API retries on a suitable fallback model
    )
    if response.stop_reason == "refusal":
        return "[The model declined this request.]"
    # The reply is a list of blocks (thinking blocks may come first), so keep only the text blocks.
    return "".join([block.text for block in response.content if block.type == "text"])


if __name__ == "__main__":
    if os.environ.get("COURSE_OFFLINE") == "1" or not os.environ.get("ANTHROPIC_API_KEY"):
        print("No API key found (or COURSE_OFFLINE=1): using the offline mock model.")
    else:
        print("API key found: using", MODEL)
    print(ask_llm("Classify the sentiment of this review in one word: <review>Great lamp, easy to use.</review>"))
