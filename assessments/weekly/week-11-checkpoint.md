# Checkpoint 11: Generative AI and Python Applications

**Week 11 · given on Day 55 · 20 minutes · closed book, no running code** · Covers Days 51–54 (+ 2 retrieval
questions from Weeks 9–10). Write your answers on paper or in a blank notebook cell (do not run them).

---

### Question 1 (predict the output)

```python
from collections import Counter

next_words = {"the": ["lamp", "lamp", "zip"], "lamp": ["is", "is"], "is": ["bright", "bright", "dim"]}
word = "the"
sentence = [word]
while word in next_words:
    word = Counter(next_words[word]).most_common(1)[0][0]
    sentence.append(word)
print(" ".join(sentence))
```

a) What is printed? b) In one sentence: what would a *higher temperature* change?

### Question 2 (predict the output)

```python
import os

os.environ["SHOP"] = "Bright Basket"
print(os.environ.get("SHOP", "none"))
print(os.environ.get("CITY", "none"))
print(os.environ.get("CITY"))
```

### Question 3 (predict the output)

```python
import json

replies = ['{"sentiment": "Positive"}', 'Sure! {"sentiment": "mixed"}', '{"sentiment": "neutral"}']
for reply in replies:
    try:
        data = json.loads(reply)
        label = data["sentiment"].lower()
        if label not in ["positive", "negative", "mixed"]:
            raise ValueError("label not allowed")
        print("ok", label)
    except ValueError:
        print("failed")
```

### Question 4 (find and fix)

Find **two** problems and rewrite the code safely (the key here is a pretend one).

```python
import anthropic

api_key = "sk-ant-..."
print("Using key", api_key)
client = anthropic.Anthropic(api_key=api_key)
```

### Question 5 (find and fix)

This function should try **at most twice** and return `None` if both replies are unusable. Find **three** bugs.

```python
def analyse(review, ask):
    while True:
        reply = ask(build_prompt(review))
        try:
            return validate_analysis(json.load(reply))
        except KeyError:
            print("Trying again")
```

### Question 6 (write code)

Write a function `build_prompt(review)` that returns a prompt asking for the sentiment of a review. It must
contain: a role, the allowed answers `positive`, `negative` or `mixed`, the instruction to answer with one word,
and the review inside `<review>` tags.

### Question 7 (write code)

a) Write a class `AlwaysBroken` with a method `ask(self, prompt)` that counts how often it was called (attribute
`calls`, starting at 0) and always returns `"Sorry!"`.
b) Write a pytest test function that checks that `analyse_review(text, ask=...)` (from Day 54) returns `None` and
called the model exactly twice when the model is always broken.

### Question 8 (explain in words)

A colleague says: *"Our prompt says 'Answer with one word: positive, negative or mixed', so our code does not need
to check the answer."* Give **two** reasons why the code must still check it.

### Question 9 (retrieval, Week 9)

`df = pd.read_csv("reviews.csv")` has the columns `review_id`, `product`, `rating`, `review_text`. Write one line
of pandas that shows the **average rating per product**, and one line that shows **how many reviews each product
has**.

### Question 10 (retrieval, Week 10)

A decision tree scores 99% accuracy on the training data and 61% on the test data.
a) What is this problem called? b) Name one way to reduce it.

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-11-checkpoint.md`_
