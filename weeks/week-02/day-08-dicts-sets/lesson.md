# Day 08: Dictionaries and Sets

**Week 2 · Session 8 of 60 · Planned 75 min** · Previous: [Day 07](../day-07-list-methods-tuples/lesson.md) · Next: [Day 09](../day-09-conditionals/lesson.md)

## Objectives

By the end of this lesson students can:

1. Model a record (a contact, a student) as a dictionary and read a value by its key.
2. Look a key up safely with `in` or `.get(key, default)`, and explain a `KeyError`.
3. Add, update and delete entries, and inspect a dictionary with `.keys()`, `.values()`, `.items()`.
4. Read values from a dictionary holding a list, a list of dictionaries and a nested dictionary.
5. Remove duplicates with `set()` and compare two groups with `|`, `&` and `-`.
6. Choose between list, tuple, dict and set for a given situation.

**Prior knowledge (Days 02–07):** f-strings and `:.2f` (Days 04–05), lists, `in`, `len/sum/min/max` (Day 06),
`.append`, `.index`, `sorted()`, `.split()`, tuples and unpacking, `None` (Day 07).

**New today besides dicts and sets:** `list(...)` as a conversion (like `int(...)`), used to turn `.items()` into a
list; single quotes for keys inside a double-quoted f-string (`f"{student['name']}"`).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: a phone book in a list | core |
| 0:05–0:14 | Dictionary basics, `KeyError`, `in`, `.get()` | core |
| 0:14–0:20 | Add, update, delete | core |
| 0:20–0:26 | `.keys()`, `.values()`, `.items()`, `list()` | core |
| 0:26–0:34 | Records: dict with a list, list of dicts, nested dict | core |
| 0:34–0:44 | Sets: de-duplicate, `.add`, `in`, `\|` `&` `-` | core |
| 0:44–0:48 | Common mistakes + choosing a structure | core |
| 0:48–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) with a Venn diagram on the board | optional (90-min session) |
| +5 min | Students design a dict for their own "profile card" from Day 02 | optional (90-min session) |

**For 60 min:** show only the list of dicts in the records section (skip the nested dict), skip `list(.items())`,
and set Exercises 1–3 and 5 in class.

## 1. Warm-up (5 min)

Demo section 0. Put a phone book in a list: `["Asha", "555-0142", "Bilal", "555-0178", ...]`. Ask students to get
Bilal's number with Day 07 tools. Answer: `contacts[contacts.index("Bilal") + 1]`.

Then ask: "What happens to every lookup if someone inserts a name in the wrong place?" (*Everything shifts, and
we get the wrong numbers with no error.*) Yesterday's Exercise 6 (removing from two parallel lists) had the same
smell. We want to look up **by name**.

## 2. Dictionary basics (9 min)

```python
phone_book = {"Asha": "555-0142", "Bilal": "555-0178", "Sara": "555-0193"}
phone_book["Bilal"]   # '555-0178'
len(phone_book)       # 3 (pairs, not 6 items)
```

> **Analogy:** a cloakroom. You hand over the ticket (the **key**) and get your coat (the **value**). You never ask
> for "the third coat on the rail". Keys are unique: two coats cannot share a ticket.

Draw the two-column key → value table from demo section 1.

**Missing keys** (demo section 2). **Prediction question:** "What happens with `phone_book["Zara"]`?" →
`KeyError: 'Zara'`. Two ways to avoid it:
- `"Zara" in phone_book` → `False` (check first; tomorrow `if` makes this automatic);
- `phone_book.get("Zara", "not saved")` → `'not saved'`. Without a default, `.get` gives `None`.

**Prediction question:** `"555-0142" in phone_book`. (*`False`: `in` on a dict checks keys only.*)

## 3. Add, update, delete (6 min)

```python
phone_book["Zara"] = "555-0101"   # new key → added
phone_book["Asha"] = "555-0199"   # existing key → replaced
del phone_book["Sara"]            # removed
stock["apples"] += 24             # update a number value in place
```

**Prediction question** (before the Asha line): "Will there be two Asha entries?" (*No. Same line, two meanings:
add if new, replace if existing.*)

## 4. Looking inside (6 min)

Demo section 4 uses a café menu `prices = {"tea": 2.50, "samosa": 1.20, ...}`:

```python
min(prices.values())        # 1.2
sum(prices.values())        # 9.45
sorted(prices)              # ['cake', 'juice', 'samosa', 'tea']  (sorted keys)
list(prices.items())[0]     # ('tea', 2.5)
item, price = list(prices.items())[0]
```

Say explicitly: `list(...)` converts, just as `int(...)` and `str(...)` did on Day 03. Each item is a **tuple**,
which is why Day 07 unpacking works. Promise: on Day 12 we loop over `.items()` and visit every pair.

## 5. Records (8 min)

**A dict can hold a list** (demo section 5):

```python
student = {"name": "Sara", "id": "S014", "marks": [78, 85, 92], "enrolled": True}
student["marks"][1]              # 85
student["marks"].append(88)      # the list inside changes
f"{student['name']}"             # single quotes inside double quotes
```

**Prediction question:** `student["marks"][1]`. Teach students to read chained brackets **left to right**, saying
each step aloud: "student, its marks, item 1".

**A list of dicts** = rows of a table (demo section 6). `class_list[1]["name"]` → `'Omar'`. Mention this is
exactly what CSV rows will look like in Week 8.

**A nested dict**: `contacts["Bilal"]["city"]` → `'Karachi'`. Keep it to reading and changing one value.

## 6. Sets (10 min)

**Why:** a sign-up form where people click twice; "how many *different* people?" (demo section 7).

```python
signups = ["Asha", "Omar", "Asha", "Mei", "Omar", "Asha"]
set(signups)           # {'Asha', 'Mei', 'Omar'} (order may vary)
len(set(signups))      # 3
sorted(set(signups))   # ['Asha', 'Mei', 'Omar']  (back to a tidy list)
```

Key points:
- No duplicates, **no order**, therefore **no indexes** (`tags[0]` → `TypeError: 'set' object is not subscriptable`).
- `.add(x)` (not `.append`); adding something already there does nothing.
- `in` works as for lists.
- `set("banana")` gives the unique letters. We use this on Day 10 to check whether a password contains a digit.
- The printed order of a set can differ between machines. Always show sets to people via `sorted()`.

**Comparing groups** (demo section 8): draw two overlapping circles labelled Python and AI.

```python
python_class & ai_class   # in both          → ['Omar', 'Sara']
python_class | ai_class   # in at least one  → 6 people
python_class - ai_class   # Python, not AI   → ['Asha', 'Bilal']
```

**Prediction question:** `ai_class - python_class`. (*`['Diego', 'Mei']`: difference depends on the order.*)

## 7. Common mistakes and choosing a structure (4 min)

Run demo section 9:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `phone_book["bilal"]` | `KeyError: 'bilal'` | keys must match exactly, including capitals |
| `phone_book[0]` | `KeyError: 0` | dictionaries have no positions; 0 is treated as a key |
| `phone_book.get["Asha"]` | `TypeError: 'builtin_function_or_method' object is not subscriptable` | `.get` is a method: round brackets |
| `languages = {}` then `.add(...)` | `AttributeError: 'dict' object has no attribute 'add'` | `{}` is an empty dict; an empty set is `set()` |
| `tags[0]` on a set | `TypeError: 'set' object is not subscriptable` | sets have no order. Use `sorted(tags)` first |
| `student["marks"] = 80` meaning "add a mark" | no error; the list is replaced by a number | change the list *inside*: `student["marks"].append(80)` |

Finish with the "which structure?" table in demo section 10 (list / tuple / dict / set) and the small enrolment
example that combines a dict of lists with sets.

## 8. Practice (22 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | lookup, `in`, `.get`, `sorted`, sets | recall |
| 2 Contact book | add / update / delete / safe lookup | application |
| 3 Fix the broken code | five dict/set mistakes | modification |
| 4 Student record | dict holding lists; list of dicts | application |
| 5 Course enrolments overlap | `set()`, `&`, `\|`, `-`, `.add` | problem solving |
| 6 Who missed the quizzes? (challenge) | combining set operations into a dict report | challenge |

While circulating, look for:
- `contacts.append(...)` / `contacts.add(...)` on a dict;
- counting `len(python_signups)` (the list, with duplicates) instead of the set;
- f-string quote clashes in Exercise 4: `f"{student["name"]}"` (works in Python 3.12+, but teach single quotes);
- `student["marks"] = 80` instead of `.append(80)`.

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 9. Recap and exit ticket (5 min)

Recap (students supply):
1. A dict maps keys to values; `d[k]` reads, `d[k] = v` adds or updates, `del d[k]` deletes.
2. Missing key → `KeyError`; use `k in d` or `d.get(k, default)`.
3. Values can be lists or other dicts; read brackets left to right.
4. A set holds unique values; `set(list)` removes duplicates; `| & -` compare groups.

**Exit ticket:** what does this print?

```python
ages = {"Mei": 19, "Ken": 22}
ages["Mei"] = 20
ages["Zara"] = 18
print(len(ages), ages.get("Omar", 0), sorted({"b", "a", "b"}))
```

Answer: `3 0 ['a', 'b']`.

## Homework (20 min)

1. Finish Exercises 5–6.
2. Build a dictionary describing your favourite film or book (title, year, a list of three main characters, a
   rating out of 10). Print a short f-string summary, change the rating, add one character, and print the
   number of characters.

## Next class

Day 09: **decisions**. Today we kept writing "check with `in` first". Tomorrow `if` lets the program make that check
itself: *if* the key is in the dictionary, look it up, *else* print a friendly message. We also meet the comparison
operators (`==`, `<`, `>=`…) and build a grade calculator.

## Instructor notes

- Do not loop over dictionaries today (Day 12). If a student asks "how do I print every contact?", show
  `print(contacts)` and promise loops.
- Do not teach `.update()`, `.pop()` on dicts, `.setdefault()`, dict comprehensions or frozen sets.
- Keys should be strings (or numbers) in this course. If someone tries a list as a key they get
  `TypeError: unhashable type: 'list'`; say "keys must be unchangeable values" and move on.
- Fictional phone numbers use the `555-01xx` pattern. Keep real personal data out of examples.
- Fast students: ask them to explain why `3.0 in menu` is `False` but `3.0 in menu.values()` is `True`.
  Slow students: let them draw a two-column key → value table before writing any code.
