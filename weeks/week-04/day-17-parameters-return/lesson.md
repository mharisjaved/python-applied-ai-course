# Day 17: Parameters, Arguments and Return Values

**Week 4 · Session 17 of 60 · Planned 75 min** · Previous: [Day 16](../day-16-functions-intro/lesson.md) · Next: [Day 18](../day-18-scope-defaults/lesson.md)

## Objectives

By the end of this lesson students can:

1. Write a function with one or more parameters, call it with arguments, and use the words *parameter* and *argument* correctly.
2. Call a function with positional and with keyword arguments, and explain when keyword arguments make a call clearer.
3. Use `return` to hand a value back, store it in a variable and use it in further calculations.
4. Explain the difference between `print` and `return`, and predict when a function gives back `None`.
5. Return two values from a function and unpack them into two variables.

**Prior knowledge:** `def`, calling, docstrings (Day 16); f-strings and `:.2f` (Days 04–05); tuples and
unpacking (Day 07); `if`/`elif` (Day 09); loops over dicts with `.items()` (Day 12).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: Day 16 exit ticket + homework look | core |
| 0:05–0:14 | Parameters and arguments (demo 1) | core |
| 0:14–0:20 | Positional and keyword arguments (demo 2) | core |
| 0:20–0:28 | `return` (demo 3) | core |
| 0:28–0:40 | `print` vs `return`, `None` (demo 4–5) | core |
| 0:40–0:47 | `return` ends the function; returning two values (demo 6–7) | core |
| 0:47–0:50 | Common mistakes (demo 8) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Grade report (demo 9) + Exercise 6 together | optional (90-min session) |
| +5 min | Students rewrite one homework function from Day 16 to take a parameter | optional (90-min session) |

**For 60 min:** skip demo 2's mixing example and demo 9; shorten demo 7 to one cell; practice Exercises 1–4 only
(Exercise 5 becomes homework).

## 1. Warm-up (5 min)

Re-run the Day 16 exit ticket on the board (`cheer()` called in a loop). Then ask two students to show the
function they extracted from their Quiz Game for homework. Ask the class: "This prints the rules for *one* quiz.
What if we wanted it to show a different quiz title each time?" That is today's first idea.

Retrieval: "What does `name, score = ("Asha", 91)` do?" (*unpacks the tuple: `name` gets `"Asha"`, `score` gets
`91`, Day 07*). We use exactly this at the end of today.

## 2. Parameters and arguments (9 min)

**Why.** Yesterday's `print_receipt_header()` always printed *CORNER CAFE*. A second café would need a second,
almost identical function: the duplication problem again.

> **Analogy: a form with blanks.** The `def` line is a form with labelled blanks (`shop_name: ______`). The
> **parameter** is the label on the blank. The **argument** is what you write in the blank each time you fill the
> form in.

Live code (demo section 1):

```python
def print_receipt_header(shop_name):
    """Print a receipt header for the shop called shop_name."""
    print("=" * 30)
    print(f"  {shop_name}")
    print("=" * 30)

print_receipt_header("CORNER CAFE")
print_receipt_header("BOOK NOOK")
```

Trace the first call on the board: "When the call runs, Python does `shop_name = "CORNER CAFE"` and then runs the
body." Parameters are just variables that get their value from the call.

**Prediction question:** `greet("Sara")` then `greet("Diego")` (demo section 1). (*`Hello, Sara! Welcome back.`,
`Hello, Diego! Welcome back.`*)

Write the vocabulary table on the board and keep it there all lesson:

| parameter | argument |
|-----------|----------|
| name in the `def` line | value in the call |
| `shop_name` | `"CORNER CAFE"` |

## 3. Positional and keyword arguments (6 min)

Demo section 2: `print_order(item, quantity, size)`.

- **Positional:** `print_order("latte", 2, "large")` → `2 x large latte`. First argument → first parameter.
- **Prediction question:** "What does `print_order(2, "latte", "large")` print?" (*`latte x large 2`. No error,
  just nonsense: Python matches by position, not by meaning.*)
- **Keyword:** `print_order(size="small", item="tea", quantity=3)` → `3 x small tea`. Order no longer matters,
  and the call explains itself.
- **Mixing** is allowed, but positional arguments come first: `print_order("mocha", size="medium", quantity=1)`.

Students have already used keyword arguments without the name: `enumerate(items, start=1)` (Day 12). Point it out.

When to use keyword arguments: when a function has several parameters of the same type (three numbers!) or when
the meaning of a value is not obvious from the call.

## 4. `return` (8 min)

**Why.** So far functions only *do* something (print). Most useful functions *calculate* something and give it
back: a converted unit, a grade, a price.

Live code (demo section 3):

```python
def km_to_miles(km):
    """Return the distance km converted to miles."""
    return km * 0.621371

distance = km_to_miles(10)
print(distance)                      # 6.21371
total = km_to_miles(3) + km_to_miles(7)
```

Explain the **substitution picture**: when the call finishes, the call itself is *replaced by the returned value*.
`km_to_miles(3) + km_to_miles(7)` becomes `1.864113 + 4.349597`. Write it on the board like an algebra step.

**Prediction question:** `celsius_to_fahrenheit(100)` (*`212.0`, a float because of `/`*).

## 5. `print` vs `return` and `None` (12 min)

This is the **number one misconception of the whole week**. Go slowly.

Demo section 4 defines two functions: `add_service_print(bill)` prints `bill + bill * 0.1`;
`add_service(bill)` returns it. Calling either one alone in a notebook *looks the same*. Then:

```python
total = add_service_print(50)    # shows 55.0 on the screen
print("total is:", total)        # total is: None
each = total / 2                 # TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
```

Ask the 🤔 question *before* running the second line. Most students will say `55.0`. Then run the returning version:
`total = add_service(50)` → `each = total / 2` → `27.5`.

> **Analogy:** `print` is a waiter **telling** you the price. You heard it, but you cannot do maths with something
> you only heard. `return` **hands you the receipt**. You can keep it, split it, add it to another one.

Rule of thumb to write on the board: **functions that calculate should `return`. The caller decides whether to
print.** Printing inside the function is for functions whose *job* is to display something (like
`print_receipt_header`).

`None` (demo section 5): every function returns *something*; without a `return` it is `None`, the value meaning
"nothing". Show `result = print_divider()` → `None`, `type(result)` → `<class 'NoneType'>`.

**Prediction question:** `print(print("hi"))` (*`hi` then `None`: the inner `print` shows `hi` and returns `None`,
which the outer `print` shows*). Students love this one.

## 6. `return` ends the function; returning two values (7 min)

Demo section 6: `letter_grade(score)` with plain `if`s and a `return` in each. Ask "why don't we need `elif`
here?" (*the first `return` that runs ends the function*). Then `is_passing(score)` returns a comparison directly:
`return score >= 50` gives `True`/`False`.

Demo section 7: `apply_discount(price, percent)` ends with `return price - saving, saving`.

```python
result = apply_discount(80, 25)      # (60.0, 20.0): a tuple
new_price, saved = apply_discount(80, 25)
print(f"Pay {new_price:.2f}, you save {saved:.2f}")   # Pay 60.00, you save 20.00
```

Key point: `return` runs **once**. `return a` followed by `return b` never returns `b`. To give back two things,
put both in one `return`, separated by a comma.

## 7. Common mistakes (3 min)

Demo section 8, plus the `None` crash from section 4:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| Using the result of a function that only prints | `TypeError: unsupported operand type(s) ... 'NoneType'` | "Where is the `return`?" No `return` means `None` |
| Calling a returning function and ignoring the value | none, the value is thrown away | Store it (`miles = ...`) or print it |
| `km_to_miles()` | `TypeError: km_to_miles() missing 1 required positional argument: 'km'` | Every parameter needs an argument |
| `km_to_miles(5, 10)` | `TypeError: km_to_miles() takes 1 positional argument but 2 were given` | Count the blanks on the form |
| `print_order(item="tea", 2, "small")` | `SyntaxError: positional argument follows keyword argument` | Positional arguments first, keyword ones after |
| `return` indented inside a loop | none, wrong answer (stops after the first item) | Indentation decides *when* the function ends (Exercise 3d) |

Notebook trap: the last line of a cell is displayed automatically, so `km_to_miles(10)` alone *seems* to print.
In a `.py` file it shows nothing. That is why demo section 8 adds `print("done")` after the call.

## 8. Practice (20 min)

Students open `practice.ipynb`. Walk around and look for:
- `print` inside a function that should `return` (look for `None` in their output);
- a function that ignores its parameter (overwrites it, or uses a variable from outside);
- `return` indented inside the loop (Exercise 3d);
- missing docstrings.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict: print or return? | `print` vs `return`, `None` | recall |
| 2 Unit converter | parameters + `return` | application |
| 3 Fix the broken code | print vs return, ignored parameter, missing argument, early return | modification |
| 4 Attendance status | `return` from branches, using the result in a loop | application |
| 5 Split the bill | keyword arguments, returning two values | problem solving |
| 6 Clock time (challenge) | `//` `%`, three return values, two inverse functions | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 9. Recap and exit ticket (5 min)

Ask students to supply the recap:
1. Parameters are the names in the `def` line; arguments are the values in the call.
2. Keyword arguments match by name; positional ones by order (and come first).
3. `return` hands a value back and ends the function; without it, the function gives back `None`.
4. Calculate → `return`; the caller decides what to print.

**Exit ticket:** what does this print?

```python
def double_print(n):
    print(n * 2)

def double_return(n):
    return n * 2

a = double_print(4)
b = double_return(4)
print(a, b)
```

Answer: `8` (printed while `a = ...` runs), then `None 8`.

## Homework (25 min)

1. Finish Exercises 5–6.
2. Write `discount_price(price, member)` that returns the price with 10% off when `member` is `True`, otherwise
   the full price. Call it four times with different arguments, including one call using keyword arguments.

## Next class

Day 18 asks "where do variables live?" (local vs global **scope**), adds **default values** for parameters
(`def add_tax(amount, rate=0.10)`), and builds a price calculator out of **small functions that call each other**.
Today's "return, don't print" rule is what makes that composition possible.

## Instructor notes

- Do **not** introduce default parameter values or scope today, even if a student asks why a variable inside a
  function "disappears". Say "great question, that's tomorrow".
- Avoid the phrase "return prints the value". Some students will say it. Correct it every time: return *gives back*;
  only `print` shows.
- If a student asks whether `print` returns anything: yes, `None`. That is what `print(print("hi"))` shows.
- `*args`, `**kwargs`, type hints and lambdas are out of scope for the whole course; don't show them.
- Floats: `0.1 + 0.2` style surprises can appear (for example `40 * 1.15`). If one shows up, say "computers store
  decimals approximately; we round when we display money" and use `:.2f`. Don't go deeper.
- Fast students: Exercise 6, then ask them to make `letter_grade` return both the letter *and* whether it passed.
  Slow students: do Exercise 1 with them and draw the "waiter vs receipt" picture again; then Exercise 2.
