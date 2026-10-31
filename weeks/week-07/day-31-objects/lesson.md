# Day 31: Objects, State and Behaviour

**Week 7 · Session 31 of 60 · Planned 75 min** · Previous: [Day 30](../../week-06/day-30-project-expense-tracker/lesson.md) · Next: [Day 32](../day-32-classes/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain "everything in Python is an object": every value has a **type**, some **state** (the data it holds) and
   **behaviour** (the methods you can call on it).
2. Use `type()` on any value and say whether a method **changes** the object (`list.append`) or **returns a new
   value** (`str.upper`).
3. List the state and behaviour of a real-world thing (a bank account, a pet, a library book).
4. Model a thing with a dict plus functions that take that dict.
5. Name at least three problems with the dict-plus-functions approach, which is the motivation for classes tomorrow.

**Prior knowledge:** string and list methods (Days 04, 07), dicts and `.get` (Day 08), mutability and aliasing
(Day 07), functions with parameters/return (Days 16–18), `raise ValueError` (Day 25), `assert` (Day 29).
Students have just finished Project 03 (Expense Tracker), where their expenses were dicts passed between functions.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:07 | Warm-up: Project 03 look-back + method recall | core |
| 0:07–0:20 | Everything is an object: type, state, behaviour (demo 1) | core |
| 0:20–0:27 | State and behaviour of real-world things (demo 2, pairs) | core |
| 0:27–0:38 | A bank account as a dict + functions (demo 3) | core |
| 0:38–0:48 | Where it gets messy: four pain points (demo 4) | core |
| 0:48–0:70 | Practice exercises 1–4 | core |
| 0:70–0:75 | Recap, class teaser (demo 5) and exit ticket | core |
| +15 min | Exercise 5 (challenge) together: a safe `transfer` between two dict accounts | optional (90-min session) |

**For 60 min:** show only pain points 2 and 3 in section 4 and set Exercise 4 as homework.

## 1. Warm-up (7 min)

Ask two or three students: "In your Expense Tracker, what did one expense look like in the code?" (*A dict such as
`{"date": ..., "category": ..., "amount": ...}`, and functions such as `add_expense(expenses, ...)` that received it.*)
Keep that answer on the board; today we look at that style critically.

Quick recall (hands up, no laptops):
- "`name = "asha"`. What does `name.upper()` give, and what is `name` afterwards?" (*`"ASHA"`; `name` is still `"asha"` because strings never change.*)
- "`marks = [70, 80]`. After `marks.append(90)`, what is `marks`?" (*`[70, 80, 90]`; lists change in place.*)

## 2. Everything is an object (13 min)

**Why this matters:** for 30 days students have written `text.strip()` and `marks.append(90)` without asking what
the dot means. Today's idea gives that dot a name: the value on the left is an **object**, and the word after the
dot is one of its **methods**.

> **Analogy:** an object is like a phone. It has **state** (battery level, contacts, volume) and **behaviour**
> (call, charge, mute). You do not open the phone to change the battery number yourself; you press buttons
> (methods) and the phone updates its own state.

Live code (demo section 1):

```python
name = "asha khan"
print(type(name))      # <class 'str'>
print(name.title())    # Asha Khan
print(name)            # asha khan   (unchanged: str methods return a NEW string)

marks = [72, 85]
marks.append(90)
print(marks)           # [72, 85, 90]  (changed: list methods often change the list itself)
```

**Prediction question:** `result = marks.append(64)` then `print(result)`. (*`None`. `append` changes the list and
returns nothing. Students who wrote `marks = marks.append(...)` in Week 2 lost their list for exactly this reason.*)

Then show that **every** value is an object with a type, even numbers and functions:

```python
print(type(42), type(3.5), type(True), type(None))
print((4.0).is_integer())   # True: even a float has methods
print(type(print))          # <class 'builtin_function_or_method'>
```

Key points:
- Notice the word **class** in `<class 'str'>`. A class is the *kind* of object. Tomorrow we write our own.
- **State** = the data inside the object (`[72, 85, 90]`). **Behaviour** = the methods (`append`, `sort`, `count`).
- Some methods **change the object** (list `append`, `sort`, dict `update`). Others **return a new value**
  and leave the object alone (all string methods, `list.count`). When unsure, print the object again.

## 3. State and behaviour of real-world things (7 min)

Pair activity, 3 minutes, then collect on the board (demo section 2 has the table):

| Thing | State (what it *has* / *is*) | Behaviour (what it *does* / what you *do to it*) |
|-------|------------------------------|--------------------------------------------------|
| Bank account | owner, balance | deposit, withdraw, show balance |
| Pet | name, species, hunger, energy | feed, play, sleep |
| Library book | title, author, on loan? | borrow, return |

Rule of thumb students will reuse on Day 34: **nouns and adjectives → state; verbs → behaviour.**
Ask for the *type* of each piece of state (`balance` is a `float`, `on loan?` is a `bool`). This connects the
table to code.

## 4. A bank account as a dict + functions (11 min)

**Intuition:** we already know how to store several related values (a dict) and how to package behaviour
(functions). Let's combine them. Live code (demo section 3):

```python
def create_account(owner, balance=0):
    return {"owner": owner, "balance": balance}

def deposit(account, amount):
    if amount <= 0:
        raise ValueError("Deposit must be more than 0.")
    account["balance"] += amount

def withdraw(account, amount):
    if amount > account["balance"]:
        raise ValueError("Not enough money in the account.")
    account["balance"] -= amount

def describe_account(account):
    return f"{account['owner']}: balance {account['balance']:.2f}"

asha = create_account("Asha", 100)
deposit(asha, 50)
withdraw(asha, 30)
print(describe_account(asha))   # Asha: balance 120.00
```

**Prediction question:** "`deposit` has no `return`. How does `asha` change?" (*A dict is mutable and the function
receives the **same** dict, not a copy. This is the Day 07 name-tag idea.*)

Create a second account (`omar = create_account("Omar")`) and show that the two dicts are independent. Then say:
"It works. So why would anyone want something else?"

## 5. Where it gets messy (10 min)

Demo section 4 shows four problems. Let students name each before you reveal it.

| # | Pain point | What you show | Error / symptom |
|---|------------|---------------|-----------------|
| 1 | Data and behaviour live apart | every call needs the dict passed in: `deposit(asha, 50)` | nothing says which functions "belong" to accounts |
| 2 | Nothing protects the state | `asha["balance"] = -500` and `asha["balanse"] = 1000` | no error at all: a negative balance, and a typo silently creates a new key |
| 3 | Name clashes as the program grows | add a pet with its own `describe(...)`, then reuse the name | the second `def describe` replaces the first → `KeyError: 'name'` for accounts |
| 4 | Any dict fits any function | `deposit(rex, 10)` where `rex` is a pet | `KeyError: 'balance'`, only discovered when the line runs |

Pain point 2 is the important one: `deposit` checks its amount, but nothing forces anyone to use `deposit`.
Pain point 3 leads to names like `describe_account`, `describe_pet`, `feed_pet`, `play_with_pet`: the type name
is glued onto every function by hand.

**Prediction question** for pain point 2: after `asha["balanse"] = 1000`, what does `describe_account(asha)` show?
(*Still the old balance. The typo created a separate key, `balanse`, that nothing reads.*)

## 6. Common mistakes

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `marks = marks.append(90)` | later `TypeError: 'NoneType' object ...` | `append` changes the list and returns `None`; don't reassign |
| `name.upper()` alone, expecting `name` to change | no error, `name` unchanged | strings never change; write `name = name.upper()` |
| `account[balance]` (no quotes) | `NameError: name 'balance' is not defined` | dict keys here are strings, so they need quotes |
| Passing the wrong dict to a function | `KeyError: 'balance'` | the function trusts that you pass the right "shape"; nothing checks it |

## 7. Practice (22 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Does the method change the object? | predicting method behaviour, `type()` | recall |
| 2 State and behaviour | modelling a real-world thing as a dict | application |
| 3 A pet as a dict + functions | functions that read/change a dict, `raise` | application |
| 4 Spot the dict problems | finding and fixing pain points 2–4 | modification |
| 5 Safe transfer (challenge) | combining functions, keeping state valid, `assert` | challenge |

Expected: everyone finishes 1–3; most finish 4; fast students try 5.

Circulate and look for:
- `feed(pet)` with a `return pet` and then `pet = feed(pet)`: it works, but ask *why* the return is not needed;
- `if pet["energy"] < 3: print("too tired")` instead of `raise`: point back to Day 25, a function should *signal* a problem, not just print;
- Exercise 4: students who fix the symptom (change the number) without naming the cause. Ask "which pain point is this?"

## 8. Recap, teaser and exit ticket (5 min)

Recap (students supply the sentences):
1. Every Python value is an object: it has a type, state (data) and behaviour (methods).
2. Some methods change the object (lists), others return a new value (strings).
3. A dict + functions can model a thing, but the data is unprotected, every function needs the dict passed in, and
   names clash as programs grow.

Show demo section 5, a three-line teaser, **without explaining the syntax**:

```python
class Account:
    def __init__(self, owner):
        self.owner = owner
```

Then `asha = Account("Asha")`, `print(asha.owner)` and `print(type(asha))` → `<class '__main__.Account'>`. "We just
made our own type, like `str` or `list`. Tomorrow you will learn every word of those three lines."

**Exit ticket:** name the state and two behaviours of a *library card*, and give one reason a dict version could go wrong.
Answer (example): state: owner, card number, books on loan; behaviour: borrow, return; risk: someone writes
`card["books"] = 99` or misspells a key and nothing stops it.

## Homework (20 min)

Finish Exercise 4. Then pick one dict from your Expense Tracker and write three lines in a markdown cell: its state,
two functions that are really its behaviour, and one thing that could make that dict invalid.

## Next class

Day 32 introduces `class`, `__init__`, `self` and attributes: a way to stamp out objects that all have the same
shape, so `asha.balance` replaces `asha["balance"]`. Today's pain points 1 and 3 are solved tomorrow;
pain point 2 (protecting state) is solved with methods and validation on Day 33.

## Instructor notes

- Do **not** teach the `class` syntax today beyond the teaser. The point of the session is the *need*.
- If a student asks "is a function really an object?", say yes: you can store it in a variable or a list. Do not
  go further (no functions as arguments, no lambdas).
- Avoid `id()`, `dir()` and memory talk. If someone discovers `dir("hi")`, say it lists the methods and move on.
- Be honest that dicts are not "bad": for simple records (one expense, one CSV row next week) dicts are perfect.
  Classes pay off when data and the rules about it belong together.
- Strong students: ask them to add a `history` list to the dict account and record every deposit/withdraw;
  then ask how many functions had to change.
