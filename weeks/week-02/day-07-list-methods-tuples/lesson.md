# Day 07: List Methods, Tuples and Mutability

**Week 2 · Session 7 of 60 · Planned 75 min** · Previous: [Day 06](../day-06-lists/lesson.md) · Next: [Day 08](../day-08-dicts-sets/lesson.md)

## Objectives

By the end of this lesson students can:

1. Choose the right list method to add (`.append`, `.insert`), remove (`.remove`, `.pop`), find (`.index`, `.count`) or reorder (`.sort`, `.reverse`) items.
2. Explain why `my_list = my_list.sort()` loses the list, and use `sorted()` when the original order must be kept.
3. Convert text to a list with `.split()` and a list of strings back to text with `"glue".join(...)`.
4. Create a tuple, explain when a tuple is a better choice than a list, and unpack it into variables.
5. Predict what happens when two names refer to the same list, and make an independent copy with `.copy()`.

**Prior knowledge (Days 02–06):** variables as name tags (Day 02), `//` (Day 03), string methods and the fact that
they never change the original string (Day 04), slicing (Day 05), lists, `len/sum/min/max`, changing an item, `in` (Day 06).

**New today besides the methods:** `None` (only as "the nothing value that `.sort()` gives back"; fully covered on
Day 17) and the `reverse=True` option of `.sort()` / `sorted()`.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: do methods change the value? | core |
| 0:05–0:15 | Adding and removing items | core |
| 0:15–0:20 | `.count()` and `.index()` | core |
| 0:20–0:28 | `.sort()` vs `sorted()`, the `None` trap | core |
| 0:28–0:33 | `.split()` and `.join()` | core |
| 0:33–0:41 | Tuples and unpacking | core |
| 0:41–0:47 | Two names, one list: aliasing vs `.copy()` | core |
| 0:47–0:50 | Common mistakes (live debugging) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together | optional (90-min session) |
| +5 min | Capital letters sort first; `.split(",")` vs `.split(", ")` | optional (90-min session) |

**For 60 min:** show `.reverse()` and the capital-letters sort only in passing, skip the coordinates example in
the tuple section, run the common mistakes as they come up, and set Exercises 1–4 in class.

## 1. Warm-up (5 min)

Demo section 0:

```python
name = "asha"
loud = name.upper()
print(name, loud)    # asha ASHA
```

Ask: "Did `.upper()` change `name`?" (*No: strings can't change, so string methods give back a new string.*)
Then: "Yesterday we changed a list with `marks[2] = 68`. Lists **can** change. So what might list methods do?"
Leave the question open; it is the thread through today's lesson.

## 2. Adding and removing items (10 min)

**Why:** real lists change all the time: a shopping list, a queue at a clinic, a to-do list.

Live code (demo sections 1–2):

```python
cart = ["milk", "eggs", "bread"]
cart.append("tea")        # ['milk', 'eggs', 'bread', 'tea']
cart.insert(1, "rice")    # ['milk', 'rice', 'eggs', 'bread', 'tea']
```

Show the "start empty, then append" pattern (`visitors = []`). Students will use it constantly from Day 12.

Removing:

```python
queue = ["Ken", "Zara", "Diego"]
served = queue.pop(0)     # served is 'Ken', queue is ['Zara', 'Diego']
last = queue.pop()        # last is 'Diego', queue is ['Zara']
```

Put the three-row table from demo section 2 on the board: **`.remove` takes a value, `.pop` takes a position and
gives the item back.** Mixing these up is the #1 error in practice (Exercise 3d).

**Prediction question:** `["milk", "rice", "eggs", "bread", "tea", "eggs"]` after `.remove("eggs")`: how many eggs
are left? (*One; only the first match is removed.*)

## 3. Finding: `.count()` and `.index()` (5 min)

Demo section 3: an attendance list `["P", "P", "A", "P", "L", "P", "A"]`. `.count("A")` → `2`,
`.index("A")` → `2`, so "first absence in session 3" needs `+ 1`.

Then pay off yesterday's teaser with parallel lists:

```python
top_position = marks.index(max(marks))
print(students[top_position], "scored", max(marks))   # Omar scored 95
```

Read the nested call **inside out**: first `max(marks)` is 95, then `.index(95)` is 3, then `students[3]` is Omar.

## 4. Sorting and the `None` trap (8 min)

```python
marks = [72, 85, 68, 95, 58, 77]
marks.sort()                 # [58, 68, 72, 77, 85, 95]
marks.sort(reverse=True)     # [95, 85, 77, 72, 68, 58]
prices = [4.50, 1.25, 3.00]
cheapest_first = sorted(prices)   # [1.25, 3.0, 4.5], prices unchanged
```

Explain `reverse=True` simply as "an option you can pass", and that `sorted()` accepts it too.

**Prediction question** (demo section 4): `result = marks.sort()` then `print(result)`. Most students predict the
sorted list. It prints `None`. Explain: `None` means "nothing here". `.sort()` did its job **on the list** and has
nothing to hand back.

Write this rule on the board and keep it there:

> **Methods that change the list give back `None`. Don't assign them.**
> `.append` `.insert` `.remove` `.sort` `.reverse` → use on their own line.
> `sorted()` `.count()` `.index()` `.pop()` and slices → give back a value worth saving.

Link back to the warm-up: strings can't change, so string methods *must* give back something new.

Quick aside: `sorted(["mei", "Zara", "asha", "Omar"])` → `['Omar', 'Zara', 'asha', 'mei']`. Capitals sort first.
Fix later with `.lower()` on the data; do not introduce `key=` (Day 21).

## 5. Text ↔ list: `.split()` and `.join()` (5 min)

Demo section 5:

```python
"learning python one step at a time".split()   # 7 words
"rice,lentils,onions,tea".split(",")           # ['rice', 'lentils', 'onions', 'tea']
" | ".join(items)                               # 'rice | lentils | onions | tea'
```

Analogy: `.split` is scissors (cut the text wherever you see the separator); `.join` is glue (the string *before*
the dot is the glue). Students find `", ".join(items)` backwards at first; say "glue dot join the pieces".

**Prediction question:** `", ".join(sorted(items))`. (*`lentils, onions, rice, tea`.*)

## 6. Tuples and unpacking (8 min)

**Why:** some data should never be edited piece by piece: a birthday, map coordinates, a (name, ID) pair. A tuple
is a list that cannot change, so a bug cannot accidentally change it either.

```python
birthday = (2004, 9, 17)
birthday[0]          # 2004  (indexing, slicing, len, in all work)
birthday[0] = 2005   # TypeError: 'tuple' object does not support item assignment
```

**Unpacking** (demo section 7):

```python
year, month, day = birthday
first, last = "Mei Lin".split()     # works on lists too
cup_a, cup_b = cup_b, cup_a         # the Day 02 swap, in one line
```

The count must match: `lat, lon = (31.52, 74.36, 217)` → `ValueError: too many values to unpack (expected 2)`.

**Prediction question:** the swap. Explain that the right side is built **first** as a tuple, then unpacked, so no
spare cup is needed.

## 7. Two name tags, one list (6 min)

This is where the Day 02 **name tag** picture pays off. Draw it as you go.

```python
a = 7
b = a
a = 100        # we MOVED the tag a. b still 7

cart = ["milk", "eggs"]
shared = cart
shared.append("tea")
print(cart)    # ['milk', 'eggs', 'tea']
```

Draw **one** list on the board with **two** tags (`cart`, `shared`) stuck on it. `.append` changes the list itself,
so every tag on it "sees" the change. Contrast: in the first example we *moved* a tag to a new value; in the second
we *changed the value* that both tags are stuck to.

Fix: `backup = cart.copy()` makes a second list with its own tag.

**Prediction question:** before running the `.copy()` cell, ask what `backup` will show.

## 8. Common mistakes (3 min)

Run demo section 9:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `cart = cart.append("tea")` | `AttributeError: 'NoneType' object has no attribute 'append'` (on the next use) | `.append` gives back `None`; you replaced your list with nothing |
| `marks = marks.sort()` | no error; `marks` is `None` | same rule. Use `marks.sort()` alone or `sorted(marks)` |
| `cart.remove("cheese")` | `ValueError: list.remove(x): x not in list` | you can only remove what is there. Check with `in` first (Day 09 makes that automatic) |
| `team.remove(2)` meaning "the third one" | `ValueError: list.remove(x): x not in list` | `.remove` wants a **value**; use `.pop(2)` for a position |
| `", ".join([3, 5, 8])` | `TypeError: sequence item 0: expected str instance, int found` | join only glues strings |
| `lat, lon = (31.52, 74.36, 217)` | `ValueError: too many values to unpack (expected 2)` | one name per value |
| `words = sentence.split` | `TypeError: object of type 'builtin_function_or_method' has no len()` (when used) | a method needs `()` to run |
| `backup = cart`, then changing `cart` | no error; backup changes too | two tags, one list. Use `.copy()` |

If time allows, run demo section 10 (shopping-list operations: split → append → insert → remove → pop → sort →
join; prints `Bought: onions` and `Still to buy (4): eggs, milk, rice, tea`). It is the model for Exercise 2.

## 9. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Trace the list | predicting method effects and `None` | recall |
| 2 Shopping-list operations | split → append/insert/remove/pop/sort → join | application |
| 3 Fix the broken code | `None` trap, missing `()`, unpacking, remove vs pop, tuples | modification |
| 4 Tuples and unpacking | unpack, build a new tuple, list of tuples | application |
| 5 Two names, one list | aliasing vs `.copy()`, `sorted()` keeps the original | reasoning |
| 6 Exam leaderboard (challenge) | combining `max/index/count/sorted/pop`, median | challenge |

While circulating, look for:
- `.split(",")` on `"rice, lentils, ..."`: items keep a leading space, so `.remove("lentils")` fails. Ask them to
  print the list and look closely at the quotes;
- `.pop()` without an index when the task says "first item";
- assigning the result of `.sort()` or `.append()`;
- Exercise 4: printing the whole tuple `('Karachi', 24.9)` instead of the name (needs a second index).

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 10. Recap and exit ticket (5 min)

Recap (students supply):
1. `.append/.insert` add; `.remove` (value) and `.pop` (position, gives it back) remove.
2. Methods that change a list give back `None`; `sorted()` gives a new list.
3. `.split()` cuts text into a list; `"glue".join(list)` glues it back.
4. Tuples are unchangeable records; unpack with `a, b = pair`.
5. `b = a` with a list means two tags on one list; `.copy()` makes a separate list.

**Exit ticket:** what does this print?

```python
a = [3, 1, 2]
b = a
b.append(0)
c = sorted(a)
print(a, c)
```

Answer: `[3, 1, 2, 0] [0, 1, 2, 3]`.

## Homework (20 min)

1. Finish Exercises 5–6.
2. Write a "to-do list" cell: start from the text `"call bank, buy stamps, email Sara, gym"`, split it into a list,
   add two tasks, mark one as done with `.pop()`, sort the rest and print them joined with `" / "`.

## Next class

Day 08: **dictionaries and sets**. Exercise 6 showed the pain of parallel lists (remove from both, keep positions
aligned). A dictionary keeps a name and its value **together** and lets us look things up by name instead of by
position. Sets will remove duplicates in one step.

## Instructor notes

- Keep `None` minimal: "the value meaning nothing". Do not explain return values or functions (Days 16–17).
- Do not show `del my_list[i]`, `.extend()`, `.clear()` or list `*`; they are not needed and dilute the core
  methods. `del` appears on Day 08 for dictionaries.
- Do not use `id()` or `is` to "prove" aliasing; the observable behaviour plus the drawing is enough.
- If a student asks "when would I ever want two names for one list?": it matters most when passing lists into
  functions (Day 17). For now the lesson is "know that it happens".
- Comparisons (`==`) are Day 09, so solutions are checked by matching printed output.
- Fast students: ask them to write the method rule (changes vs gives back) in their own words in a markdown cell.
  Slow students: let them print the list after **every** line of Exercise 2.
