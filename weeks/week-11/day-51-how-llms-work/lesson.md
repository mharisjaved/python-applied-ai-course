# Day 51: How LLM Apps Work

**Week 11 · Session 51 of 60 · Planned 75 min** · Previous: [Day 50](../../week-10/day-50-project-ml-predictor/lesson.md) · Next: [Day 52](../day-52-prompt-design/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain next-token prediction with the "very well-read autocomplete" picture, using a toy next-word model.
2. Describe in plain words what a token, a system message, a user message, the context window and temperature are.
3. Name three limitations of LLMs (hallucination, knowledge cut-off, no guarantee of understanding) and say why
   an app must check model output.
4. Draw the LLM app pipeline **input → prompt template → model → parse → output** and point to each step in code.
5. Write a prompt template as a function that returns an f-string, and run it through a fake model.

**Prior knowledge:** functions with `return` (Day 17), f-strings (Day 04), dicts and counting (Days 08, 12),
`random` (Day 14), `collections.Counter` (Day 26), classes (Day 33), `csv.DictReader` (Day 36), rules vs learning
and what GenAI is (Day 41), training vs prediction (Day 46).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only). Data:
`datasets/reviews.csv` (40 short product reviews, used all week and in Project 08).

**No API key today.** Everything uses a fake model written in plain Python. The real API arrives on Day 53.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: rules vs learning, training vs prediction | core |
| 0:05–0:20 | Next-token prediction with a toy model + temperature (demo 1–2) | core |
| 0:20–0:30 | Tokens, messages, context window (demo 3–4) | core |
| 0:30–0:36 | Limitations (demo 5) | core |
| 0:36–0:50 | The LLM app pipeline: template → fake model → parse (demo 6–7) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 (challenge) together, or a class discussion: "Where would you NOT trust an LLM?" | optional (90-min session) |

**60-min version:** shorten demo 3–4 to the token estimate and the messages list (skip the conversation-history
cell), and set Exercise 5 as homework.

## 1. Warm-up (5 min)

Questions (cold-call, no notebooks):
- "On Day 41 we compared *writing rules* with *learning from examples*. Which one is ML?" (*Learning from examples.*)
- "What is the difference between training and prediction?" (*Training: the model learns from labelled data.
  Prediction: we use the trained model on new input.*)
- "ChatGPT/Claude write text. What do you think they were trained to predict?" Collect guesses; today answers it.

## 2. Next-token prediction (10 min)

**Why:** students have used chat assistants and usually believe there is a database of answers or a "thinking
person" inside. The single most useful mental model for building apps is: **an LLM continues text**.

> **Analogy:** your phone keyboard suggests the next word. An LLM is a *very* well-read autocomplete: it has seen
> a huge amount of text during training and predicts the next piece of text, one piece at a time, again and again.

Live code (demo section 1): a toy model learns "which word follows which" from six sentences.

```python
corpus = ["the battery lasts all day", "the battery is great", "the battery is weak",
          "the sound is great", "the sound is clear", "the case is cheap"]
# build next_words: {"the": ["battery", "battery", "battery", "sound", "sound", "case"], "is": [...], ...}
predict_next("the")          # 'battery'  (seen 3 times after "the")
generate("the")              # 'the battery is great'
```

**Prediction question:** "What does `predict_next("is")` return?" (*`great`, seen twice; every other word once.*)

Key points:
- Our toy looks at **one** previous word. A real LLM looks at **all the text so far** and learned its patterns
  from a gigantic amount of text, but the job is the same: *predict what comes next*.
- Nothing in the model "looks up" facts. It produces text that is *likely*. That explains both why it is
  impressive and why it can be confidently wrong (section 5).

## 3. Temperature (5 min)

Live code (demo section 2): `random.choice(next_words["the"])` picks "battery" half of the time, because the list
contains it 3 times out of 6. So picking randomly from the list = picking in proportion to how likely each word is.

- **Temperature 0** ≈ always take the most likely word: the same input gives the same output.
- **Higher temperature** ≈ sample more freely: more variety, more surprises, more mistakes.
- Real chat apps sample, which is why asking the same question twice can give different answers. That matters for
  apps: **we cannot test an LLM app by running it once.**
- We do not set temperature in this course. The current Claude models choose their own sampling settings, so our
  helper never passes one. The concept is what matters.

## 4. Tokens, messages and the context window (10 min)

**Tokens** (demo section 3): models read and write *tokens*, pieces of text that are often a whole short word, part
of a longer word, or punctuation. Rule of thumb for English: **1 token ≈ 4 characters ≈ ¾ of a word**. The exact
split depends on the model, so treat our `estimate_tokens(text)` (characters ÷ 4) as a rough estimate only.
Why care? **Tokens are how models are limited and billed** (cost is Day 53's topic). Expected output of the demo:
the 40 reviews are 2,710 characters, so about 680 tokens.

**Messages** (demo section 4): a request to a chat model is data we already know how to build: a list of dicts.

```python
system = "You are a friendly assistant for an online shop. Answer in one short sentence."
messages = [{"role": "user", "content": "Is the backpack waterproof?"}]
```

- **System message:** the app's standing instructions (role, rules, tone). Written by the developer.
- **User message:** what the person typed. **Assistant message:** what the model replied earlier.
- The model has **no memory between calls**. A "conversation" works because the app sends the *whole* message list
  every time (show the three-message list in the demo).
- **Context window:** the maximum number of tokens one request can contain, *including the reply*. The course
  models allow about 1 million tokens (Oct 2026), but cost grows with every token you send, so we keep prompts small.

**Prediction question:** "A chat has gone on for 200 messages. Why might the app start to 'forget' the beginning?"
(*The history no longer fits the context window, or it is trimmed to save cost.*)

## 5. Limitations (6 min)

Demo section 5 shows a fake model that answers a question it cannot know ("The warranty is 5 years.").

| Limitation | What it means | Consequence for an app |
|------------|---------------|------------------------|
| Hallucination | fluent, confident text that is false | never show model "facts" as truth without a source or a check |
| Knowledge cut-off | it only knows what was in its training data | recent events or *your* private data must be put in the prompt |
| No guarantee of understanding | it predicts likely text; it can fail on sarcasm, maths, logic | test on many inputs, validate output |
| Randomness | same input, different output | check output format every time |
| Bias and privacy (Day 41) | learned from human text; prompts leave your computer | review outputs; never send personal data you do not need to |

Message: **the model is one unreliable component; the code around it makes the app reliable.** That is what this
week builds.

## 6. The LLM app pipeline (14 min)

Draw on the board (keep it up all week):

```
input (review) → prompt template → model → parse → output (label, report)
   csv file        f-string fn      fake_llm   split/strip   print / save
```

Live code (demo sections 6–7):
1. `build_prompt(review)`: a function returning an f-string with instructions + the review.
2. `fake_llm(prompt)`: counts a few positive/negative words and returns e.g. `"Sentiment: Positive"`.
   Stress: a *model is just a function text → text*. Swapping it for a real one later changes one line.
3. `parse_sentiment(reply)`: `"Sentiment: Positive"` → `"positive"`; anything unexpected → `"unknown"`.
4. Run all three on reviews from `reviews.csv` and compare with the star ratings (expected output: the fake model
   agrees with the stars on 25 of 40 reviews, 62%).

**Prediction question** (demo section 6): "We change the template's first line to *You are a great assistant*.
What happens to every result?" (*"great" is now in every prompt, so every score goes up by 1. The model sees the
whole prompt, instructions included; tomorrow's delimiters fix exactly this kind of mix-up.*)

## 7. Common mistakes (live, 3 min, demo section 8)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| Template without the `f` | no error! the model receives the literal text `{review}` | silent bugs are the worst: print one prompt before sending it |
| `parse` assumes a colon that is not there | `IndexError: list index out of range` | model output is not guaranteed; check before you index |
| Fake model uses `print` instead of `return` | `AttributeError: 'NoneType' object has no attribute 'split'` | Day 17: printing is not returning |
| Trusting the label without checking it is allowed | no error, wrong data in the report | validate against a list of allowed labels |

## 8. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the next word | next-token idea, temperature | recall / predict |
| 2 Messages and tokens | system/user/assistant roles, token estimate | apply |
| 3 A prompt template | f-string template function | apply |
| 4 Fix the pipeline | missing `f`, print vs return, parsing | modify / fix |
| 5 Pipeline on real reviews | input → prompt → model → parse → output | independent problem |
| 6 Teach the fake model "not" (challenge) | improving and measuring a model | challenge |

Circulate and look for: templates missing `\n` between instructions and review; comparing `"Positive"` with
`"positive"`; students hard-coding the expected string instead of building it from parameters.

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 9. Recap and exit ticket (5 min)

Recap (students supply the sentences):
1. An LLM predicts the next token again and again; temperature controls how adventurous the choices are.
2. A request is a system message plus a list of user/assistant messages, and it must fit in the context window.
3. An LLM app = input → prompt template → model → parse → output, and the code must check what the model says.

**Exit ticket:** name the five pipeline steps in order, and write one reason why step 4 (parse) is needed.
*Answer: input, prompt template, model, parse, output. The model returns free text that can have any format (or be
wrong), and the rest of the program needs a clean, checked value.*

## Homework (20 min)

Finish Exercise 5. Then write three sentences in a markdown cell: one task in your life an LLM app could help with,
which step of the pipeline would be hardest, and one way it could go wrong.

## Next class

Day 52 is about the **template** step: how to write prompts that give reliable, parseable answers (clear task,
allowed labels, output format, delimiters, examples) and how to *measure* whether a new prompt is better on a small
test set. Today's 62% agreement is the number to beat.

## Instructor notes

- Keep the theory practical. Do **not** go into neural networks, transformers, attention or training details.
  If asked, "it is a very large neural network trained on text; how it works inside is beyond this course".
- Avoid claiming the model "thinks" or "knows". Prefer "predicts", "produces", "generates".
- Token numbers are estimates. If a student asks for the exact count, say the API reports it in each response
  (`usage`), which they will see on Day 53.
- Fast students: ask them to make `generate()` stop after 6 words and try several seeds (temperature idea).
  Slow students: let them skip Exercise 2's token part and focus on Exercises 3–5, the pipeline is what matters.
- If a student asks "why not just use the chat website?": an *app* runs the same task on 1,000 reviews, the same
  way each time, with checked output. That is this week's goal (Project 08).
