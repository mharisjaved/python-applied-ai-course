# Python Readiness Assessment (end of Week 8)

**Given on Day 40** ([lesson](../../weeks/week-08/day-40-capstone-demo/lesson.md)) · **50 minutes, 50 points** ·
replaces the Week 8 checkpoint · covers Weeks 1–8.

Purpose: to check that every student can use Python **on their own** before the AI phase (Weeks 9–12), and to
decide who needs support. It is not a pass/fail exam. Results decide the help each student gets in Week 9.

## Instructions for students

- **Sections A–E (38 min): on paper.** No computer, no notes. Write code as neatly as you can; small typos do
  not cost points if the idea is right.
- **Section F (12 min): on the computer.** You may run Python and use `help()`. No notes, no internet, no AI
  assistants.
- If you are stuck on a question, move on and come back later.

| Section | Topic | Points | Suggested time |
|---------|-------|--------|----------------|
| A | Reading code (predict the output) | 8 | 6 min |
| B | Fixing bugs | 9 | 8 min |
| C | Writing functions | 10 | 10 min |
| D | Files, CSV and JSON | 8 | 7 min |
| E | A small class | 7 | 7 min |
| F | Practical task (computer) | 8 | 12 min |

---

## Section A: Reading code (8 points, 2 each)

Write **exactly** what each program prints.

**A1.**
```python
names = ["asha", "Bilal", " omar "]
cleaned = [name.strip().title() for name in names]
print(cleaned)
print(cleaned[-1][:2], len(cleaned))
```

**A2.**
```python
stock = {"pen": 12, "ruler": 0, "glue": 5}
total = 0
for item, count in stock.items():
    if count == 0:
        continue
    total += count
print(total, stock.get("tape", "none"))
```

**A3.**
```python
def add_bonus(score, bonus=5):
    score = score + bonus
    return score

score = 70
result = add_bonus(score)
print(score, result, add_bonus(score, 10))
```

**A4.**
```python
attempts = ["abc", "-3", "7", "9"]
for text in attempts:
    if not text.isdigit():
        print("skip", text)
        continue
    number = int(text)
    if number > 5:
        print("found", number)
        break
```

## Section B: Fixing bugs (9 points, 3 each)

For each function: **(1)** say what goes wrong for the example, **(2)** explain the cause in one sentence, and
**(3)** write the corrected line(s).

**B1.** `average([4, 6, 8])` should return `6.0`.
```python
def average(numbers):
    """Return the average of a list of numbers."""
    total = 0
    for n in numbers:
        total += n
        return total / len(numbers)
```

**B2.** `count_words("The cat saw the dog")` should return `{'the': 2, 'cat': 1, 'saw': 1, 'dog': 1}`.
```python
def count_words(text):
    """Return {word: count} for the words in text, ignoring upper/lower case."""
    counts = {}
    for word in text.lower().split():
        counts[word] = 1
    return counts
```

**B3.** `read_age("abc")` should raise a `ValueError`. What happens instead?
```python
def read_age(text):
    """Return text as an int age between 0 and 120, or raise ValueError."""
    try:
        age = int(text)
    except ValueError:
        print("Not a number")
    if age < 0 or age > 120:
        raise ValueError("Age out of range")
    return age
```

## Section C: Writing functions (10 points)

**C1. (5 points)** A museum charges: under 12 years → `5.0`; 12 to 64 → `12.0`, but students pay `8.0`;
65 and over → `6.0`. Write `ticket_price(age, is_student)` with a docstring. It must **return** the price, and
raise `ValueError` if `age` is negative.

**C2. (5 points)** Write `top_scorers(scores, limit)`. `scores` is a dict `{name: score}`. Return a list of the
names whose score is **at least** `limit`, in alphabetical order. Example:
`top_scorers({"Mei": 91, "Ken": 78, "Zara": 85}, 80)` returns `["Mei", "Zara"]`.
Then write **two** `assert` lines that test it: one normal case and one edge case.

## Section D: Files, CSV and JSON (8 points)

**D1. (4 points)** The file `sales.csv` contains:
```
item,quantity,price
notebook,3,2.50
"pens, blue",10,0.80
stapler,1,6.00
```
a) Write code that reads the file with the `csv` module and prints the total value of all rows
(quantity × price), formatted with 2 decimals: `Total value: 21.50`. (3 points)
b) Why would `line.split(",")` give a wrong result for this file? (1 point)

**D2. (4 points)**
a) What does this print? (2 points)
```python
import json
data = {"name": "Ken", "scores": (80, 92), "active": True, "mentor": None}
text = json.dumps(data)
print(text)
back = json.loads(text)
print(back["scores"][1] + 1, back == data)
```
b) Write `save_settings(settings, path)` that saves a dict as JSON, and `load_settings(path)` that returns the
saved dict, or `{"theme": "light"}` if the file does not exist. (2 points)

## Section E: A small class (7 points)

**E1. (6 points)** Write a class `BusPass`:
- `__init__(self, owner, rides=0)`: stores the owner's name (without extra spaces) and the number of rides.
  Raise `ValueError` for an empty owner name or a negative number of rides.
- `top_up(self, rides)`: adds rides; raise `ValueError` if `rides` is 0 or less.
- `use(self)`: uses one ride; raise `ValueError("No rides left")` if there are none.
- `__str__`: returns, for example, `Bus pass of Sara: 3 rides left`.

**E2. (1 point)** Using your class, what does this print?
```python
card = BusPass("Sara", 1)
card.use()
try:
    card.use()
except ValueError as error:
    print("Error:", error)
card.top_up(5)
print(card)
```

## Section F: Practical task (8 points, on the computer)

Create `transport_report.py`. It reads the course dataset `datasets/expenses.csv` (columns `date`, `category`,
`description`, `amount`, `payment_method`; dates look like `2026-09-01`) and:

1. has a function `load_expenses(path)` that returns a list of dicts with `amount` converted to a float;
2. has a function `monthly_totals(expenses, category)` that returns `{month: total}` for one category, where the
   month is the first 7 characters of the date and totals are rounded to 2 decimals;
3. in `main()`, saves the totals for the category `"transport"` to `transport_summary.json` (with `indent=2`) and
   prints one line per month, e.g. `2026-09: 123.45`;
4. prints a clear message instead of crashing if the CSV file cannot be found.

Run it with `uv run python transport_report.py` and hand in the file and its output.

---

_Answer key (instructor only, not published): `assessments/answer-keys/python-readiness.md`_
