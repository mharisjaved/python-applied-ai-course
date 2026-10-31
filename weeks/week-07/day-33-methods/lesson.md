# Day 33: Attributes and Methods

**Week 7 · Session 33 of 60 · Planned 75 min** · Previous: [Day 32](../day-32-classes/lesson.md) · Next: [Day 34](../day-34-composition/lesson.md)

## Objectives

By the end of this lesson students can:

1. Write methods that **read** state (return information) and methods that **change** state.
2. Call methods with parameters and use their return values; explain that `asha.describe()` means
   `Student.describe(asha)`, so `self` is `asha`.
3. Keep an object valid by raising `ValueError` inside `__init__` and other methods, and handle that error with
   `try/except ValueError as error`.
4. Add `__str__` so `print(obj)` shows a friendly description.
5. Recognise the common method mistakes: missing `self` parameter, missing `self.`, missing `()`, `__str__` that prints.

**Prior knowledge:** classes, `__init__`, `self`, attributes (Day 32), the dict-account pain points (Day 31),
`raise ValueError` and `try/except` (Day 25), return vs print (Day 17), f-string formats (Day 05).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: Day 32 exit-ticket style question | core |
| 0:05–0:15 | From function to method (demo 1) | core |
| 0:15–0:25 | Methods that change state, methods that answer (demo 2–3) | core |
| 0:25–0:37 | Validation inside methods (demo 4) | core |
| 0:37–0:44 | `__str__` (demo 5) | core |
| 0:44–0:48 | Common mistakes (demo 7) | core |
| 0:48–0:70 | Practice exercises 1–4 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Demo 6: `transfer_to` and a statement (two objects working together) | optional (90-min session) |
| +10 min | Exercise 5 (challenge) | optional (90-min session) |

**For 60 min:** skip demo 6, show only mistakes 1 and 4 in demo 7, and set Exercise 4 as homework.

## 1. Warm-up (5 min)

On the board:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

mochi = Pet("Mochi")
rex = Pet("Rex")
rex.hunger = rex.hunger - 2
print(mochi.hunger, rex.hunger)
```

(*`5 3`. Two independent instances.*) Then: "Yesterday we wrote `feed(pet)` as a function *outside* the class.
Which of Day 31's pain points does that still have?" (*The function lives apart from the data, and `feed` could
clash with another `feed`.*)

## 2. From function to method (10 min)

**Why:** a function that only makes sense for one kind of object belongs *with* that object. A **method** is a
function defined inside the class. Live code (demo section 1):

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.marks = []

    def describe(self):
        return f"{self.name} ({self.student_id}) has {len(self.marks)} marks"

asha = Student("Asha", "S001")
print(asha.describe())          # Asha (S001) has 0 marks
print(Student.describe(asha))   # the same thing, written the long way
```

Key explanation: `asha.describe()` is Python's short way of writing `Student.describe(asha)`. The object before the
dot becomes `self`. **That is all `self` is: the specific object the method is working on right now.** Call it on
`bilal` and `self` is `bilal`.

**Prediction question:** "`describe` has one parameter, `self`. How many arguments do we pass?" (*None. Python
passes the object before the dot.*)

## 3. Methods that change state and methods that answer (10 min)

Switch to the Day 31 example (demo section 2) so students see the dict version transformed:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):          # changes state
        self.balance += amount

    def withdraw(self, amount):         # changes state
        self.balance -= amount

    def can_withdraw(self, amount):     # answers a question, changes nothing
        return amount <= self.balance
```

Compare with Day 31 on the board: `deposit(asha, 50)` became `asha.deposit(50)`. The dict is no longer passed
around: the object carries its own behaviour (pain point 1 ✓). `rex.deposit(10)` now fails immediately with
`AttributeError: 'Pet' object has no attribute 'deposit'` (pain point 4 ✓), and two classes can both have a
`describe` method without clashing (pain point 3 ✓).

Two kinds of methods (demo section 3):
- **Commands** change state and usually return nothing (`deposit`). Like `list.append`.
- **Questions** return a value and change nothing (`can_withdraw`). Like `str.upper`.
- A method may also do both: `withdraw` could return the new balance. Keep it clear which one each method is.

**Prediction question:** `print(asha.deposit(50))`. (*`None`, because `deposit` has no `return`. Same lesson as
`list.append` on Day 31.*)

## 4. Validation inside methods (12 min)

**Why:** this is the answer to pain point 2. The object refuses to get into an invalid state. Demo section 4:

```python
def __init__(self, owner, balance=0):
    if balance < 0:
        raise ValueError("Opening balance cannot be negative.")
    ...

def deposit(self, amount):
    if amount <= 0:
        raise ValueError(f"Deposit must be more than 0, got {amount}.")
    self.balance += amount

def withdraw(self, amount):
    if amount <= 0:
        raise ValueError(f"Withdrawal must be more than 0, got {amount}.")
    if amount > self.balance:
        raise ValueError(f"Cannot withdraw {amount:.2f}: balance is only {self.balance:.2f}.")
    self.balance -= amount
```

Teaching points:
- **Check first, change second.** Every `raise` comes before the line that changes state, so a failed call leaves
  the object exactly as it was. Show `print(account.balance)` after a failed withdraw.
- The method raises; the **caller** decides what to do (Day 25 pattern). Recap the syntax:

```python
try:
    omar.withdraw(500)
except ValueError as error:      # `as error` gives us the exception; printing it shows its message
    print("Sorry:", error)
```

- Be honest: `asha.balance = -500` is still *possible*. The rule in this course: **change state through methods**.
  The methods are the front door; reaching in through the window is a bug. (Python has ways to enforce this, but
  they are outside this course.)

**Prediction question:** "After `omar.withdraw(500)` fails, what is Omar's balance?" (*Unchanged, because the raise
happened before the subtraction.*)

## 5. `__str__`: friendly printing (7 min)

Yesterday `print(asha)` showed `<__main__.Student object at 0x...>`. Demo section 5 adds:

```python
def __str__(self):
    return f"{self.owner}'s account: balance {self.balance:.2f}"
```

- Python calls `__str__` automatically whenever it needs the object as text: `print(account)`, `str(account)` and
  f-strings like `f"{account}"`.
- `__str__` must **return** a string, never print it (otherwise `TypeError: __str__ returned non-string`).
- Double underscores mark names that Python calls for you ("dunder" methods). `__init__` and `__str__` are the
  only two we need.
- One-line aside if asked: `__repr__` is a similar method used when an object is shown *inside a list*; we will see
  that tomorrow when we print a list of objects.

## 6. Optional: two objects working together (10 min, 90-min session)

Demo section 6: `transfer_to(self, other, amount)` calls `self.withdraw(amount)` then `other.deposit(amount)`.
Inside a method, other methods of the same object are called with `self.` in front. `self` and `other` are two
different `BankAccount` objects. The class also gets a `history` list that every deposit/withdraw appends to and a
`statement()` method that returns a multi-line string. This is a preview of objects working together (Day 34).

## 7. Common mistakes (4 min)

Run the tagged cells in demo section 7:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `def deposit(amount):` (no `self`) | `TypeError: BankAccount.deposit() takes 1 positional argument but 2 were given` | the object before the dot is always passed as the first argument |
| `balance += amount` inside a method (no `self.`) | `UnboundLocalError: cannot access local variable 'balance' ...` | without `self.` Python looks for a local variable; the attribute lives on `self` |
| `account.deposit` (no brackets) | no error, nothing happens; in a cell it shows `<bound method ...>` | without `()` you only *mention* the method; you don't call it |
| `__str__` that prints instead of returns | `TypeError: __str__ returned non-string (type NoneType)` | Python needs the text back to print it itself |
| `BankAccount.deposit(50)` (called on the class) | `TypeError: ... missing 1 required positional argument: 'amount'` | call methods on an instance: `asha.deposit(50)` |

## 8. Practice (22 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the tally counter | tracing method calls and return values | recall/predict |
| 2 `Student` gets methods | command + question methods, validation, `__str__` | application |
| 3 Fix the thermostat | the four common method mistakes | modification |
| 4 Coffee loyalty card | designing methods with a rule, `try/except` | problem solving |
| 5 Parking garage (challenge) | list attribute, several validation rules, `assert` | challenge |

Expected: everyone finishes 1–3, most finish 4, fast students try 5.

Circulate and look for:
- validation written as `print("Invalid")` followed by the change anyway: ask "after this call, is the object valid?";
- the change written *before* the check;
- `average()` crashing with `ZeroDivisionError` on a student with no marks: ask what an empty list should give;
- `__str__` that uses `print`.

## 9. Recap and exit ticket (5 min)

Recap (students supply the sentences):
1. A method is a function inside a class; `obj.method(x)` means `Class.method(obj, x)`, so `self` is `obj`.
2. Command methods change state; question methods return information.
3. Methods check before they change: `raise ValueError` keeps the object valid; the caller catches it.
4. `__str__` returns the text that `print(obj)` shows.

Tick pain points 1–4 on the board from Day 31.

**Exit ticket:** write a method `rename(self, new_name)` for `Student` that raises `ValueError` if `new_name` is
empty (after `.strip()`) and otherwise changes the name.

Answer:

```python
def rename(self, new_name):
    new_name = new_name.strip()
    if new_name == "":
        raise ValueError("Name cannot be empty.")
    self.name = new_name
```

## Homework (25 min)

Finish Exercise 4. Then add `add_stamps(self, count)` to your loyalty card, which uses a loop over `add_stamp()`,
and raises `ValueError` if `count` is not positive.

## Next class

Day 34: objects that **contain other objects** (a `Playlist` that holds `Song` objects, a `Course` that holds
`Student` objects), how to design classes from a written description, and how to test classes with `assert` and
`pytest.raises`. That is the last step before Project 04 on Day 35.

## Instructor notes

- `self` explanation that works: write `asha.describe()` and underneath `Student.describe(asha)` and draw an
  arrow from `asha` to `self`. Repeat it every time someone is confused.
- Do not teach `@property`, private attributes (`_balance`, `__balance`), `@classmethod` or `@staticmethod`. If a
  student has seen `_balance` online: "a single underscore is a polite 'please don't touch'; we use methods as the
  front door instead."
- Do not go into other dunder methods (`__eq__`, `__len__`, `__add__`). Mention `__repr__` only if asked.
- Money as `float` is fine for this course; if a strong student asks about rounding errors, say real banking
  software stores cents as integers (or uses `decimal`), and move on.
- Strong students: make `withdraw` return the new balance and discuss whether a method should both change state and
  return a value. Weaker students: give them the `BankAccount` from the demo and ask them to add only `deposit`
  validation first.
