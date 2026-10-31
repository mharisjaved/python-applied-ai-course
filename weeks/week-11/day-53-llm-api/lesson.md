# Day 53: Calling an LLM API

**Week 11 · Session 53 of 60 · Planned 75 min** · Previous: [Day 52](../day-52-prompt-design/lesson.md) · Next: [Day 54](../day-54-parsing-validation/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain what an API and an API key are, and why a key must never appear in code, a notebook or on GitHub.
2. Estimate the cost of an LLM task from token counts and per-million-token prices, and say what a rate limit is.
3. Read settings with `os.environ.get(name, default)` and load them from a `.env` file with `python-dotenv`.
4. Explain every line of `ask_llm()`: the offline check, the client, the request, the refusal check and joining
   the text blocks of the reply.
5. Catch API errors in the right order (most specific first) and fall back gracefully.

**Prior knowledge:** `try/except` and exception order (Day 25), modules and `import` (Day 26), uv and `.venv`
(Day 27), classes (Day 32–33), `Path.read_text`/`write_text` (Day 24), messages as a list of dicts and tokens
(Day 51), prompts (Day 52).

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · `llm.py` (the finished helper; today we build
it ourselves and then use this file). The course root contains `.env.example` and `.gitignore`.

**New today:** `os.environ`, `python-dotenv` (`load_dotenv`), the `anthropic` SDK, `issubclass()`.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:04 | Warm-up: exception order, what is a module | core |
| 0:04–0:10 | What an API is; request and response (demo 1) | core |
| 0:10–0:16 | Cost and rate limits (demo 2) | core |
| 0:16–0:28 | Environment variables, `.env`, `.gitignore` (demo 3–4) | core |
| 0:28–0:40 | Building `ask_llm()` step by step (demo 5–6) | core |
| 0:40–0:46 | API errors, most specific first (demo 7) + common mistakes | core |
| 0:46–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Live call with the instructor's key (section 4), Exercise 6 | optional (90-min session) |

**60-min version:** present demo 2 as a single worked example, skip the fake-response cells in demo 6 (just
explain the last three lines of `ask_llm`), and set Exercise 5 as homework.

## 1. Warm-up (4 min)

- "`except ValueError` and `except Exception`: which must come first, and why?" (*ValueError, the specific one.
  Python uses the first matching `except`, and every ValueError is also an Exception.*) We need this today.
- "What does `from llm import ask_llm` do?" (*Runs `llm.py` once and gives us its `ask_llm` function.*)

## 2. What an API is (6 min)

> **Analogy:** a restaurant waiter. You do not walk into the kitchen; you give your order (a **request**) in the
> agreed format, and the waiter brings back the dish (a **response**). An API is the waiter between our program
> and someone else's program, here a model running on Anthropic's servers.

Demo section 1 shows the request as a Python dict (model, max_tokens, system, messages; all Day 51 ideas) and what a
response contains: a list of **content blocks**, a `stop_reason` and `usage` (input and output tokens).

The **API key** is a long secret string that says "this request is from my account, bill me". Anyone who has it
can spend your money. That is the whole reason for sections 4 and 5.

## 3. Cost and rate limits (6 min)

Tokens = money. Prices are per **million** tokens, separately for input (prompt) and output (reply). Demo section 2
uses the prices listed in October 2026 (always check the current pricing page):

| Model ID | Input $/1M tokens | Output $/1M tokens |
|----------|-------------------|--------------------|
| `claude-opus-5-5` (course default) | 4.00 | 20.00 |
| `claude-haiku-5-5` (much cheaper) | 0.10 | 0.50 |

Worked example (demo): 40 reviews × ~120 input tokens and ~60 output tokens → about $0.067 with Opus, $0.0017 with
Haiku. 100,000 reviews → about $168 vs $4.20. Points:
- Output tokens cost 5× more than input tokens. Asking for one word or compact JSON is cheaper than an essay.
- The model may also spend tokens **thinking** before it answers; they count as output tokens. Our estimate is a
  minimum: check `usage` in real responses.
- **Which model the class uses is the instructor's decision** (set `LLM_MODEL` in `.env`). The code reads the model
  name from the environment, so no code changes are needed.
- **Rate limits:** each account may send only so many requests/tokens per minute. Too many → error 429
  (`anthropic.RateLimitError`). The SDK already waits and retries such errors **twice** before giving up.

## 4. Environment variables and `.env` (12 min)

**Why:** the key must reach our program without being written in the program.

Demo section 3: `os.environ` behaves like a dict of text settings that every program on the computer receives.

```python
os.environ["SHOP_NAME"] = "Mei's Gadgets"       # set (only for this running program)
os.environ.get("SHOP_NAME")                      # "Mei's Gadgets"
os.environ.get("SHOP_CITY")                      # None
os.environ.get("SHOP_CITY", "Lahore")            # "Lahore" (default)
os.environ["SHOP_CITY"]                          # KeyError, like a dict
```

Never print a key. Print whether it is set: `bool(os.environ.get("ANTHROPIC_API_KEY"))`.

Demo section 4: a `.env` file holds `NAME=value` lines, and `load_dotenv()` copies them into `os.environ`.
`load_dotenv()` looks for `.env` in the current folder, then its parent folder, and so on up, so **one `.env` in
the course root** works for every notebook. It does not overwrite variables that are already set.

**Order matters** (show it in `llm.py`): `load_dotenv()` runs at the top of the module, *before*
`MODEL = os.environ.get("LLM_MODEL", "claude-opus-5-5")`. If the order were reversed, `LLM_MODEL` from `.env` would
not exist yet and every student would silently use the default model.

Instructor live setup (terminal, course root; do it before class, show the steps):

```bash
cp .env.example .env       # Windows PowerShell: Copy-Item .env.example .env
# open .env in VS Code and paste the key after ANTHROPIC_API_KEY=  (no quotes, no spaces)
# optionally: LLM_MODEL=claude-haiku-5-5
cat .gitignore             # must contain the line .env
uv run python weeks/week-11/day-53-llm-api/llm.py
```

The last command prints which mode is active (mock or real model) and one reply. Then restart the notebook kernel.

**`.gitignore`:** the list of files Git (the tool that uploads code to GitHub) must never track. The course
`.gitignore` already contains `.env`. Bots scan GitHub for leaked keys within minutes; a leaked key must be
**revoked** in the console immediately, deleting the file is not enough. `.env.example` (no values) *is* shared,
so others know which settings exist.

## 5. Building `ask_llm()` step by step (12 min)

Demo section 5 grows the function in three steps (keep the board drawing from Day 51; only the *model* box changes):

1. **Offline only:** `return mock_llm(prompt)`, which is all Days 51–52 needed.
2. **Choose:** if `COURSE_OFFLINE` is `"1"` or there is no key, use the mock. Otherwise call the API. (The
   course checker sets `COURSE_OFFLINE=1`, so notebooks never spend money during automatic checks.)
3. **The real call** (exactly as in `llm.py`):

```python
client = anthropic.Anthropic()              # reads ANTHROPIC_API_KEY from os.environ by itself
response = client.beta.messages.create(
    model=MODEL,                            # exact model ID string, from LLM_MODEL
    max_tokens=16000,                       # upper limit for the reply (a safety limit, not a target)
    system=system,
    messages=[{"role": "user", "content": prompt}],
    betas=["server-side-fallback-2026-07-01"],
    fallbacks="default",                    # if this model declines, the API retries on a suitable fallback model
)
if response.stop_reason == "refusal":
    return "[The model declined this request.]"
return "".join([block.text for block in response.content if block.type == "text"])
```

Explain:
- `client.beta...` + `betas=[...]`: the automatic fallback is a *beta* feature, so we name it.
- `stop_reason == "refusal"`: the model (and its fallback) declined; there is no useful text, so return a clear
  message instead of crashing.
- The reply is a **list of blocks**. A *thinking* block may come first and has no `.text`, so
  `response.content[0].text` is a bug. Demo section 6 shows this offline with small fake classes (Week 7 OOP!).
- Official examples often write `"".join(block.text for ...)` without square brackets; it works the same.

**Prediction question:** "No key, no `COURSE_OFFLINE`. What does `ask_llm("Hi")` return?" (*The mock's reply: it
never reaches the client line.*)

## 6. API errors (6 min)

Demo section 7: `issubclass(anthropic.RateLimitError, anthropic.APIStatusError)` is `True`, so the order of `except`
clauses matters exactly as on Day 25:

| Exception | Meaning | What the app should do |
|-----------|---------|------------------------|
| `anthropic.AuthenticationError` | key missing/invalid/revoked (401) | tell the user to check `.env`; never print the key |
| `anthropic.RateLimitError` | too many requests (429), even after the SDK's 2 retries | wait and try later, or slow down |
| `anthropic.APIConnectionError` | no connection (no internet, firewall) | check the connection, try later |
| `anthropic.APIStatusError` | any other error answer from the API (`.status_code`) | report the status code |

`safe_ask(prompt)` in the demo catches them in this order and returns `None`, so the caller can count a failure
instead of crashing. Errors cannot be triggered offline, so practice Exercise 5 simulates one with Python's built-in
`ConnectionError`.

**Common mistakes**

| Mistake | Symptom | How to explain it |
|---------|---------|-------------------|
| Key pasted into a cell | the key is saved in the `.ipynb` and pushed to GitHub | keys live only in `.env`; revoke a leaked key |
| `print(os.environ.get("ANTHROPIC_API_KEY"))` | key visible on the projector / in outputs | print `bool(...)` instead |
| `os.environ["LLM_MODEL"]` when unset | `KeyError` | use `.get(name, default)` |
| `.env` edited after the kernel started | still uses the mock | restart the kernel (load happens on import) |
| `response.content[0].text` | `AttributeError` on a thinking block | keep only blocks whose `type == "text"` |
| `except anthropic.APIStatusError` first | the rate-limit branch never runs | most specific first |

## 7. Practice (24 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the environment | `os.environ`, `.get` with default, `KeyError` | recall / predict |
| 2 What will it cost? | cost formula, comparing models | apply |
| 3 Fix the leaky notebook | secure key handling | modify / fix |
| 4 Your own `ask_llm` | offline fallback, the real call | apply |
| 5 When the call fails | `try/except`, exception order | independent problem |
| 6 Settings checker (challenge) | reading `.env.example`/`.gitignore` safely | challenge |

Circulate and look for: anyone typing a real key into a notebook (stop them kindly, explain revoking);
`os.environ.get("ANTHROPIC_API_KEY") == True` (it is a string, not a bool); cost formulas that forget "per million".

## 8. Recap and exit ticket (5 min)

Recap:
1. An API key identifies and bills your account: keep it in `.env`, keep `.env` in `.gitignore`, never print it.
2. Cost = input tokens × input price + output tokens × output price (per million). Rate limits → 429 → retries.
3. `ask_llm()` uses the mock when offline or without a key; otherwise it calls Claude, checks for a refusal and
   joins only the text blocks.
4. Catch API errors most specific first.

**Exit ticket:** a classmate writes `api_key = "sk-ant-..."` in a cell and pushes the notebook to GitHub. List two
things that are now necessary. *Answer: revoke the key in the console and create a new one; move the key into
`.env` (listed in `.gitignore`) and read it with `os.environ`/`load_dotenv`; remove it from the notebook (and its
history).*

## Homework (20 min)

Finish Exercise 5. Copy `llm.py` into your own uv project (Day 27), add `.env.example` and a `.gitignore` with
`.env`, and run `uv run llm.py` to see "using the offline mock model".

## Next class

Day 54: the model's reply is still just *text*. We ask for **JSON**, turn it into a dict with `json.loads`, check
every field, retry once with a stricter prompt, and test it all with a `MockLLM` class that misbehaves on purpose.

## Instructor notes

- **Never** show your key on the projector. Prepare `.env` before class and only show `bool(...)`.
- Decide the model before the course (Haiku is far cheaper for a class) and set a spending limit in the console.
- Students do not need keys; everything works with the mock. If some students have keys, they use their own, never
  a shared class key in a chat message.
- Do not go into HTTP, JSON over the wire, streaming, async or tool use. If asked, "the SDK does all of that for us".
- `client.beta.messages.create` (not `client.messages.create`) is deliberate: it is the endpoint that accepts the
  fallback beta. Strong students can read about structured output (`output_config`) in the SDK docs as an extension;
  the course validates JSON itself on Day 54 because that works with any model and with the mock.
