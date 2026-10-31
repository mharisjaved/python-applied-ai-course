"""Review Insights Assistant (Project 08 starter).

Reads datasets/reviews.csv, removes personal data, asks an LLM to analyse every review as JSON, validates each
reply, and prints a report. Without an API key, llm.py answers with the offline mock model.

Work through the TODOs in order (1 to 6). After each one, run the tests:
    uv run pytest -q          (from this folder)
Run the program:
    uv run app.py
"""

import csv
import json
from collections import Counter
from pathlib import Path

import anthropic

from llm import ask_llm

DATA_PATH = Path(__file__).parent / "../../../datasets/reviews.csv"
RESULTS_PATH = Path(__file__).parent / "results.json"
ALLOWED_SENTIMENTS = ["positive", "negative", "mixed"]
REQUIRED_KEYS = ["sentiment", "topics", "summary"]
PUNCTUATION = ".,!?;:()\"'"
STRICT_REMINDER = ("\nYour previous reply could not be used. "
                   "Return ONLY the JSON object: no other text and no code fences.")


def load_reviews(path=DATA_PATH):
    """Return a list of review dicts: review_id, product, rating (int) and review_text."""
    # TODO 1: read the CSV with csv.DictReader (Day 36). For every row, append a dict with the four keys.
    #         Convert the rating with int(). Strip spaces from the text.
    #         Extra: skip rows with an empty text or a rating that is not a whole number (try/except).
    return []


def redact(text):
    """Replace e-mail addresses with [EMAIL] and phone-like numbers with [PHONE]."""
    # TODO 2: work word by word: text.split(), then " ".join(...) at the end.
    #         For each word, remove punctuation around it first: core = word.strip(PUNCTUATION)
    #         - an e-mail has an "@" with text before it and a "." somewhere after it
    #         - a phone number has at least 7 digits, and mostly digits (count them with .isdigit())
    #         Replace only the core, so punctuation stays: word.replace(core, "[PHONE]")
    #         Tip: two small helper functions, looks_like_email(word) and looks_like_phone(word), keep this short.
    return text


def build_prompt(product, text):
    """Return the prompt for one review. The text must be redacted inside this function."""
    # TODO 3: return an f-string (Day 52) that
    #         - says which product the review is about,
    #         - puts redact(text) between <review> and </review> tags and says to treat it as data,
    #         - asks for ONLY a JSON object with the keys "sentiment" ("positive", "negative" or "mixed"),
    #           "topics" (a list of at most 3 short lowercase topics) and "summary" (one short sentence).
    return ""


def parse_response(reply):
    """Turn the model's reply into a clean dict with sentiment, topics and summary.

    Raise ValueError if the reply cannot be used.
    """
    # TODO 4 (Day 54): take the text from the first "{" to the last "}" and json.loads it (no braces -> ValueError).
    #         Check: it is a dict, all REQUIRED_KEYS exist, sentiment (stripped, lowercase) is allowed,
    #         topics is a list of non-empty strings, summary is a non-empty string.
    #         Return a NEW dict with the cleaned values (lowercase sentiment and topics, at most 3 topics).
    raise ValueError("TODO 4: parse_response is not written yet")


def analyse_all(reviews, ask=ask_llm):
    """Analyse every review. Return (results, failed_ids); a failure must never stop the run.

    Each result is a dict with: review_id, product, rating, sentiment, topics, summary.
    `ask` is the model (any function prompt -> text). Tests pass a mock model here.
    """
    # TODO 5: for each review:
    #         - prompt = build_prompt(...), reply = ask(prompt), analysis = parse_response(reply)
    #         - if parse_response raises ValueError, try ONCE more with prompt + STRICT_REMINDER
    #         - if it fails again, add the review_id to failed_ids and continue with the next review
    #         - optional (live API): also catch anthropic.APIConnectionError and anthropic.APIStatusError
    #         Tip: a helper analyse_one(review, ask) that returns the analysis or None keeps this short.
    results = []
    failed_ids = []
    return results, failed_ids


def make_report(results, failed_ids):
    """Return the report as one string (main() prints it).

    Required lines (the tests look for them exactly):
        Reviews analysed: 38 (failed: 2)
          backpack: positive 4, negative 3, mixed 1        (one line per product, sorted by name)
          quality: 11                                      (top 5 topics, then top 5 topics of
                                                            negative and mixed reviews)
    """
    # TODO 6: count sentiments per product (a dict of dicts), count topics with collections.Counter,
    #         build a list of lines and return "\n".join(lines).
    return "TODO 6: make_report is not written yet"


# --- Should ---------------------------------------------------------------------------------------

def find_disagreements(results):
    """Return the results where the stars and the text disagree (4-5 stars but negative, 1-2 stars but positive)."""
    # TODO (Should): loop over results and collect the ones that disagree.
    return []


def save_results(results, failed_ids, path=RESULTS_PATH):
    """Save the results and the failed IDs as JSON: {"results": [...], "failed": [...]}."""
    # TODO (Should): json.dump(..., file, indent=2) (Day 36).
    pass


def main():
    reviews = load_reviews()
    if not reviews:
        print("load_reviews() returned no reviews yet: start with TODO 1.")
        return
    print(f"Loaded {len(reviews)} reviews. Analysing...")
    results, failed_ids = analyse_all(reviews)
    print()
    print(make_report(results, failed_ids))

    print()
    print("Stars and text disagree (check these by hand):")
    for result in find_disagreements(results):
        print(f"  {result['review_id']} {result['rating']} stars, {result['sentiment']}: {result['summary']}")
    save_results(results, failed_ids)


if __name__ == "__main__":
    main()
