# Day 18: Scope, Default Values and Composition

**Week 4 · Session 18 of 60 · Planned 75 min** · Previous: [Day 17](../day-17-parameters-return/lesson.md) · Next: [Day 19](../day-19-decomposition/lesson.md)

## Objectives

By the end of this lesson students can:

1. Predict which variable a function uses when a local and a global variable share a name, by drawing the two "whiteboards" (scopes).
2. Explain why a variable created inside a function cannot be used outside it, and get values out with `return` instead.
3. Explain why a function should not rely on, or change, global variables, and rewrite such code to pass values in and return them out.
4. Give a parameter a default value, call the function with and without that argument, and put default parameters in the right order.
5. Build a bigger result from small functions that call each other (composition), and trace the chain of calls.

**Prior knowledge:** `def`, docstrings (Day 16); parameters, keyword arguments, `return`, `None`, print vs
return (Day 17); `sum` (Day 06); f-string format specs `:.2f` and `:,` (Day 05).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: print vs return retrieval | core |
| 0:05–0:20 | Local scope with whiteboard diagrams (demo 1–2) | core |
| 0:20–0:28 | Global variables: reading constants vs hidden inputs vs changing them (demo 3–4) | core |
| 0:28–0:37 | Default parameter values (demo 5) | core |
| 0:37–0:47 | Composition: the price calculator (demo 6) | core |
| 0:47–0:50 | Common mistakes (demo 7) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +5 min | `*args` box and the "mutable default" question (see Instructor notes) | optional (90-min session) |
| +10 min | Exercise 6 together | optional (90-min session) |

**For 60 min:** skip the `round`/`sep` cell in demo 5 and the "hidden input" cell in demo 3 (mention it in words);
show demo 7 mistake 4 only; practice Exercises 1–4.

## 1. Warm-up (5 min)

On the board:

```python
def add_five(n):
    print(n + 5)

x = add_five(10)
print(x)
```

"What appears?" (*`15`, then `None`.*) "Fix it so `x` is 15." (*`return n + 5`.*) Today we lean on this rule
constantly: values leave a function **only** through `return`.

## 2. Local scope (15 min)

**Why.** Day 16 ended with a cliffhanger: the menu list inside `show_menu` could not be used outside. Today we
explain why, and why that is a *feature*.

> **Analogy: each call gets a fresh whiteboard.** When a function is called, Python gives it a clean whiteboard.
> Parameters and every variable created in the body are written there. When the function returns, the whiteboard
> is **wiped**. Only the returned value is carried out. The notebook (or file) has its own big board, the
> **global** board, which everyone can read.

Live code (demo section 1): `make_greeting("Zara")` works; `print(message)` afterwards gives
`NameError: name 'message' is not defined`. Draw the two boards (they are in the demo markdown too):

```
GLOBAL                                  while make_greeting("Zara") runs
┌──────────────────────────────┐        ┌───────────────────────────┐
│ make_greeting → (function)   │        │ name    → "Zara"          │
└──────────────────────────────┘        │ message → "Hi Zara!"      │
                                        └───────────────────────────┘
```

Demo section 2, **same name, different variables**: a global `total = 0` and a function `add_up(prices)` that
also uses a variable `total`.

**Prediction question:** `print(add_up([3, 4, 5]))` then `print(total)`. (*`12`, then `0`. Two different
variables called `total`, one on each board.*)

Trace it with the class: draw both boards and update the local `total` column (0 → 3 → 7 → 12) while the global
one stays 0. Then state the lookup rule: **a function looks on its own whiteboard first, then on the global board.**

Why is this a feature? Because you can use any variable names inside a function without worrying about breaking
the rest of the program. 200 lines of Quiz Game in one scope is exactly where name clashes happen.

## 3. Global variables (8 min)

Three cases, in demo section 3–4:

1. **Reading a global constant** (`SERVICE_RATE = 0.10`, `UPPER_CASE`, never reassigned): fine. This is how
   Project 02 will use `MAX_WRONG = 6`.
2. **Reading a global that changes** (`discount`): 🤔 `sale_price(100)` gives `80`, then after `discount = 50`
   the *same call* gives `50`. A hidden input. Fix: make `discount` a parameter.
3. **Changing a global** (`visitors = visitors + 1` inside `add_visitor()`):
   `UnboundLocalError: cannot access local variable 'visitors' where it is not associated with a value`.

Explaining case 3 without jargon: "Because the function **assigns** to `visitors`, Python decides `visitors`
lives on the function's own whiteboard. Then it tries to read it before anything was written there."

Mention the `global` keyword exists (it is in a markdown cell in the demo, not run) and why we avoid it: any
function could change the value at any time, the bug shows up far from its cause, and you cannot check the
function on its own. The better pattern, written on the board:

```python
def add_visitor(count):
    return count + 1

visitors = add_visitor(visitors)     # pass in, return out, store
```

## 4. Default parameter values (9 min)

**Why.** Many calls use the same value for an argument (tax is nearly always 10%). Typing it every time is noise;
leaving it out should "just work".

Live code (demo section 5):

```python
def add_tax(amount, rate=0.10):
    """Return amount plus tax at rate (10% unless told otherwise)."""
    return amount + amount * rate

print(add_tax(200))           # 220.0
print(add_tax(200, 0.05))     # 210.0
print(add_tax(200, rate=0))   # 200
```

"You have used defaults since Week 1": `round(3.14159)` → `3` vs `round(3.14159, 2)` → `3.14`; `print` puts a
space between values unless you pass `sep=" | "` (new for most students, show it as an example only).

**Prediction question:** the three `name_tag(...)` calls in demo section 5 (*`Ken | Student | Python Club`,
`Mei | Mentor | Python Club`, `Omar | Student | Hack Day`*). The third shows how a **keyword argument skips a
default** you want to keep.

Rule: parameters **with** defaults come **after** those without (otherwise `SyntaxError`, demo section 7).

## 5. Composition: the price calculator (10 min)

**Why.** Real programs are many small functions that call each other. Each one is easy to write, read and check.

Live code (demo section 6): four one-job functions (`subtotal`, `apply_discount(amount, percent=0)`, `add_tax`,
`format_money`) and one function that combines them:

```python
def checkout_total(prices, discount_percent=0):
    """Return the amount to pay for a list of prices, formatted as text."""
    amount = subtotal(prices)
    amount = apply_discount(amount, discount_percent)
    amount = add_tax(amount)
    return format_money(amount)
```

**Prediction question:** `checkout_total([450, 1200, 350])` and with `discount_percent=10`.
(*`2,200.00` and `1,980.00`.*)

Draw the call chain (it is in the demo):

```
checkout_total([450, 1200, 350], 10)
 ├─ subtotal(...)              → 2000
 ├─ apply_discount(2000, 10)   → 1800.0
 ├─ add_tax(1800.0)            → 1980.0
 └─ format_money(1980.0)       → "1,980.00"
```

Key points: each function returns to its caller (Day 16's "jump in, come back" picture, one level deeper);
`checkout_total` reads like a recipe; to change how money is shown we edit **one** small function.

**Optional box (`*args`):** read the box at the end of demo section 6 aloud in 30 seconds. Students only need to
recognise the syntax if they meet it online. Do not write any code with it.

## 6. Common mistakes (3 min)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| Using a local variable outside its function | `NameError: name 'message' is not defined` | The whiteboard was wiped. `return` the value and store it |
| Assigning to a global inside a function | `UnboundLocalError: cannot access local variable ...` | Assignment makes the name local. Pass it in, return it out |
| `def name_tag(role="Student", name):` | `SyntaxError: parameter without a default follows parameter with a default` | Required parameters first, defaults last |
| A middle function forgets `return` | `TypeError: ... 'NoneType' ...` reported in a **later** function | The error shows where `None` *arrived*, not where it was *made*. Ask "where did the `None` come from?" |
| Calling `add_points(score, 10)` without `score = ...` | none; the value is thrown away | A returned value must be stored |

Demo section 7, mistake 4, is worth the time: it is the first time students see an error message with several
arrows (one per function call). Do not teach traceback reading in depth (Day 28); just show that the arrows follow
the call chain.

## 7. Practice (20 min)

Students open `practice.ipynb`. Walk around and look for:
- `global` appearing anyway (copied from the internet). Ask them to pass the value in and return it;
- `add_points(score, 10)` without storing the result (Exercise 3);
- composed functions that recompute instead of calling the small ones (Exercise 4: `order_total` should call
  `item_total` and `shipping_cost`);
- forgetting to pass a value on to an inner function (Exercise 6: `min_length`).

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the scope | local vs global, hidden inputs, defaults | recall |
| 2 Greetings with defaults | default values, keyword arguments | application |
| 3 Fix the global counter | replace a global change with pass-in/return-out | modification |
| 4 Shipping calculator | composition with defaults | application |
| 5 Student summary | composition, decisions, f-string formatting | problem solving |
| 6 Password strength (challenge) | several small checks combined, passing defaults on | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 8. Recap and exit ticket (5 min)

Ask students to supply the recap:
1. Variables made inside a function (and its parameters) are local and disappear when it returns.
2. Functions may read global constants, but should get everything else through parameters and give results back
   with `return`. Avoid `global`.
3. Default values make arguments optional; defaults go last.
4. Big results come from small one-job functions calling each other.

**Exit ticket:** what does this print?

```python
discount = 5

def final_price(price, discount=10):
    return price - discount

print(final_price(50), final_price(50, 20), discount)
```

Answer: `40 30 5`. The parameter `discount` (default 10) is local and hides the global one; the global stays 5.

## Homework (25 min)

1. Finish Exercises 5–6.
2. Take one function from your Day 16 or Day 17 homework and give one of its parameters a sensible default value.
   Write three calls: one using the default, one positional, one keyword.

## Next class

Day 19 is about **planning** a program as functions before writing it (top-down design and pseudocode) and
**checking** each function with `print(f(x) == expected)`. We build a text-statistics tool and then plan Hangman
together for Project 02. Today's composition is the core skill.

## Instructor notes

- Keep the vocabulary simple: "local", "global", "whiteboard". Do not introduce LEGB, enclosing scopes, nested
  functions or `nonlocal`.
- Optional visualisation: Python Tutor (pythontutor.com) draws the frames for short snippets. Nice for the
  `add_up` example if you have a projector and internet access; not required.
- **Mutable default values** (`def add_item(item, basket=[])`): do not raise this. If a strong student asks,
  answer: "a list default is created *once* and shared between calls, so use `basket=None` and create the list
  inside". Keep it to that sentence.
- Students may ask whether lists passed into a function can be changed by it (`.append` inside a function). Yes:
  the function receives the same list (Day 07 aliasing). We rely on this lightly in Hangman (`guessed_letters`).
  Prefer returning new values in their own code for now.
- `*args` / `**kwargs` stay out of scope (named only in the optional box).
- Fast students: Exercise 6, then ask them to add a `"very strong"` level for passwords of 12+ characters,
  reusing `is_long_enough` with a different `min_length`. Slow students: Exercise 1 with you at the board (draw
  the whiteboards), then Exercises 2 and 3.
