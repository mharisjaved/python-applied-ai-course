# Building LLM Apps

**What it is:** a Python program that builds a prompt, sends it to a large language model (or an offline mock), then parses and validates the reply.
**Why it exists:** LLMs can read and write free text (summaries, classification, extraction), but their raw replies are unreliable text, so the code around them matters as much as the model.

**Taught on:** [Day 51](../../weeks/week-11/day-51-how-llms-work/lesson.md) (pipeline, mock) ·
[Day 52](../../weeks/week-11/day-52-prompt-design/lesson.md) (prompt design) ·
[Day 53](../../weeks/week-11/day-53-llm-api/lesson.md) (API, `.env`) ·
[Day 54](../../weeks/week-11/day-54-parsing-validation/lesson.md) (JSON validation, `MockLLM`) · reviewed on
[Day 59](../../weeks/week-12/day-59-capstone-reliability/lesson.md)

## The pipeline

```text
user input → build prompt (template) → model (real API or mock) → parse reply (json.loads) → validate fields → output / fallback
```

**Prompt checklist (Day 52):** ☐ one clear task · ☐ the context the model needs · ☐ user text inside delimiters
(`<review>…</review>`) · ☐ exact output format (JSON keys and allowed values) · ☐ 1–3 examples for tricky cases
(few-shot) · ☐ what to answer when unsure · ☐ tested on several inputs, including edge cases (one word, sarcasm, off-topic).

**API facts:** model IDs are exact strings: `claude-opus-5-5` (course default) or the much cheaper `claude-haiku-5-5`,
chosen with `LLM_MODEL` in `.env`. The key lives in `.env` (`ANTHROPIC_API_KEY=…`), which is listed in `.gitignore`;
copy the course's `.env.example`. The SDK already retries rate-limit (429) and server (5xx) errors twice. A reply is a
list of blocks (a thinking block may come first): never use `response.content[0].text`. Without a key, or with
`COURSE_OFFLINE=1`, everything runs on the mock.

**API errors** (catch the most specific first): `anthropic.AuthenticationError` (bad or missing key) →
`anthropic.RateLimitError` (too many requests) → `anthropic.APIConnectionError` (no internet) →
`anthropic.APIStatusError` (any other HTTP error; has `.status_code`).

## Examples

### 1. The course helper: `ask_llm()` (Day 53)

```python
import os

import anthropic
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY and LLM_MODEL from a .env file if present (must run before MODEL)
MODEL = os.environ.get("LLM_MODEL", "claude-opus-5-5")


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
    return "".join(block.text for block in response.content if block.type == "text")
```

### 2. Prompt template and a deterministic mock (Day 51–52)

```python
# (continues from example 1)
import json


def build_prompt(review):
    return f"""Classify the sentiment of the product review between <review> tags.
Reply with JSON only, for example {{"sentiment": "positive", "confidence": 0.9}}.
sentiment must be one of: positive, negative, mixed.

<review>
{review}
</review>"""


def mock_llm(prompt):
    """Offline stand-in for the model: keyword rules, same answer every time."""
    text = prompt.lower()
    if "stopped" in text or "broke" in text or "refund" in text:
        return json.dumps({"sentiment": "negative", "confidence": 0.8})
    if "great" in text or "love" in text:
        return json.dumps({"sentiment": "positive", "confidence": 0.8})
    return json.dumps({"sentiment": "mixed", "confidence": 0.5})


print(ask_llm(build_prompt("Great sound and I love the case.")))   # {"sentiment": "positive", "confidence": 0.8}
```

### 3. Validate the reply: `json.loads` + field checks (Day 54)

```python
# (continues from example 2)
ALLOWED = ["positive", "negative", "mixed"]


def parse_sentiment(reply):
    """Turn the model's text into a checked dict, or raise ValueError."""
    start, end = reply.find("{"), reply.rfind("}")   # rfind = find, searching from the right
    if start == -1 or end == -1:
        raise ValueError("no JSON object in reply")
    try:
        data = json.loads(reply[start:end + 1])
    except json.JSONDecodeError:
        raise ValueError("reply is not valid JSON")
    if data.get("sentiment") not in ALLOWED:
        raise ValueError(f"unexpected sentiment: {data.get('sentiment')}")
    confidence = data.get("confidence")
    if type(confidence) not in (int, float) or not 0 <= confidence <= 1:
        raise ValueError("confidence must be a number from 0 to 1")
    return {"sentiment": data["sentiment"], "confidence": confidence}


for reply in ['{"sentiment": "positive", "confidence": 0.9}',
              'Sure! Here it is: {"sentiment": "negative", "confidence": 0.7}',
              '{"sentiment": "angry", "confidence": 0.7}']:
    try:
        print("OK:", parse_sentiment(reply))
    except ValueError as error:
        print("Rejected:", error)
# OK: {'sentiment': 'positive', 'confidence': 0.9}
# OK: {'sentiment': 'negative', 'confidence': 0.7}
# Rejected: unexpected sentiment: angry
```

### 4. Retry with a fallback, tested with a `MockLLM` (Day 54)

```python
# (continues from example 3)
class MockLLM:
    """Fake model for tests: returns prepared replies in order and remembers the prompts."""

    def __init__(self, replies):
        self.replies = replies
        self.prompts = []

    def ask(self, prompt):
        self.prompts.append(prompt)
        return self.replies.pop(0)


def analyse(review, ask=ask_llm, attempts=2):
    """Ask the model, validate, retry if the reply is invalid; never crash."""
    for attempt in range(attempts):
        try:
            return parse_sentiment(ask(build_prompt(review)))
        except ValueError as error:
            print(f"Attempt {attempt + 1} rejected: {error}")
    return {"sentiment": "unknown", "confidence": 0.0}


fake = MockLLM(["It is negative.", '{"sentiment": "negative", "confidence": 0.8}'])
result = analyse("Stopped charging after a week.", ask=fake.ask)   # Attempt 1 rejected: no JSON object in reply
assert result == {"sentiment": "negative", "confidence": 0.8}
assert len(fake.prompts) == 2
print(analyse("I love it, great value."))   # {'sentiment': 'positive', 'confidence': 0.8}   (real model or mock)
```

`ask=fake.ask` swaps the model for the mock's method (like `key=get_points` on Day 21), so the test runs offline
and gets the same replies every time.

## Safety and privacy checklist

☐ No API key in code, notebooks, screenshots or Git (only in `.env`) · ☐ remove or mask personal data (names,
emails, phone numbers) before sending text to an API · ☐ treat every reply as untrusted: validate it, never run it as
code · ☐ check facts against your own data (hallucination) and say in the UI that the output is AI-generated ·
☐ test on varied inputs for unfair or biased answers · ☐ develop with the mock; limit how many real calls a run can
make (cost, rate limits) · ☐ a fallback when the API fails or the reply is invalid.

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `response.content[0].text` | `AttributeError`, or empty text, when the first block is a thinking block | Join the blocks whose `type == "text"` (as `ask_llm` does) |
| `json.loads(reply)` with no checks | `JSONDecodeError` on "Sure! Here it is: {…}", or missing keys later | Extract `{…}`, `json.loads`, check every field |
| Typo in the model ID (`claude-opus-5.5`) | `anthropic.NotFoundError` (404) | Copy the exact ID: `claude-opus-5-5` |
| Key pasted into the notebook | key leaks when you share or commit | `.env` + `load_dotenv()`; `.env` in `.gitignore` |
| `load_dotenv()` after reading `LLM_MODEL` | `.env` model setting ignored | Call `load_dotenv()` at the top, before `MODEL = …` |
| Tests that call the real API | slow, cost money, fail offline, different answer every run | Pass a `MockLLM` with fixed replies |
| User text pasted into the prompt without delimiters | the review's own words get treated as instructions | Wrap it: `<review>…</review>` |

## See also

- [01 AI vocabulary](01-ai-vocabulary.md): tokens, context window, temperature, hallucination
- [14 CSV and JSON](../python/14-csv-and-json.md): `json.loads` and JSON ↔ Python types
- [11 Exceptions](../python/11-exceptions.md) · [13 Classes](../python/13-classes.md) · [12 Testing](../python/12-modules-uv-and-testing.md)
