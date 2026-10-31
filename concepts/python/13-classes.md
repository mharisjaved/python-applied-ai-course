# Classes and Objects

**What it is:** a class is a blueprint that bundles data (attributes) and behaviour (methods); each object made from it is an instance.
**Why it exists:** a dict plus loose functions gets messy as programs grow. A class keeps the data and the code that changes it together, and can keep that data valid.

**Taught on:** [Day 31](../../weeks/week-07/day-31-objects/lesson.md) (objects, state and behaviour) ·
[Day 32](../../weeks/week-07/day-32-classes/lesson.md) (`class`, `__init__`, `self`) ·
[Day 33](../../weeks/week-07/day-33-methods/lesson.md) (methods, `__str__`, validation) ·
[Day 34](../../weeks/week-07/day-34-composition/lesson.md) (composition)

## Syntax at a glance

| You want to… | Write | Note |
|--------------|-------|------|
| Define a class | `class Product:` | class names use `CapitalWords` |
| Set up each new object | `def __init__(self, name, price):` | runs automatically when you create an object |
| Store data on the object | `self.name = name` | an *attribute* |
| Create objects (instances) | `pen = Product("Pen", 1.5)` | do **not** pass `self` |
| Read / change an attribute | `pen.price`, `pen.price = 2.0` | |
| Behaviour | `def restock(self, amount):` inside the class | a *method*: first parameter is always `self` |
| Call a method | `pen.restock(10)` | Python fills in `self` for you |
| Nice `print()` output | `def __str__(self): return f"…"` | must **return** a string |
| Refuse bad data | `raise ValueError("price cannot be negative")` inside a method | |
| An object inside an object | `self.items = []` then `self.items.append(product)` | composition: a cart *has* products |

**Dict vs class:** `student["name"]` becomes `student.name`; `add_mark(student, 90)` becomes `student.add_mark(90)`.

## Examples

### 1. A class and two independent instances

```python
class Student:
    """One student and their marks."""

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.marks = []


asha = Student("Asha", 2)
omar = Student("Omar", 1)
asha.marks.append(91)
print(asha.name, asha.marks)   # Asha [91]
print(omar.name, omar.marks)   # Omar []
print(type(asha))              # <class '__main__.Student'>
```

### 2. Methods that change state, return values and validate

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        return self.balance

    def __str__(self):
        return f"{self.owner}: {self.balance:.2f}"


account = BankAccount("Sara", 50)
print(account.deposit(25))   # 75
print(account)               # Sara: 75.00
try:
    account.deposit(-10)
except ValueError as error:
    print("Rejected:", error)   # Rejected: deposit must be positive
```

### 3. A method that calculates from the object's data

```python
class Runner:
    def __init__(self, name, times):
        self.name = name
        self.times = times          # minutes for each 5 km run

    def best(self):
        return min(self.times)


zara = Runner("Zara", [31.5, 29.0, 30.2])
print(zara.name, zara.best())   # Zara 29.0
```

### 4. Composition: a classroom *has* students

```python
class Learner:
    def __init__(self, name):
        self.name = name
        self.days_present = 0

    def mark_present(self):
        self.days_present += 1


class Classroom:
    def __init__(self, title):
        self.title = title
        self.learners = []

    def add(self, learner):
        self.learners.append(learner)

    def report(self):
        for learner in self.learners:
            print(f"{learner.name:<6}{learner.days_present}")


room = Classroom("Python 101")
mei = Learner("Mei")
ken = Learner("Ken")
room.add(mei)
room.add(ken)
mei.mark_present()
mei.mark_present()
ken.mark_present()
room.report()
# Mei   2
# Ken   1
```

**Inheritance** (`class Teacher(Person):`) is only an optional Day 34 preview; this course uses composition.

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Forgot `self` in a method: `def report():` | `TypeError: Classroom.report() takes 0 positional arguments but 1 was given` | `def report(self):` |
| `name = name` instead of `self.name = name` | `AttributeError: 'Student' object has no attribute 'name'` | Store it on `self` |
| Typo in `__init__` (`__init`, `_init_`) | `TypeError: Student() takes no arguments` | Two underscores on each side: `__init__` |
| `__str__` prints instead of returning | `TypeError: __str__ returned non-string (type NoneType)` | `return f"…"` |
| No `__str__` | `print(obj)` shows `<__main__.Product object at 0x…>` | Add a `__str__` method |
| Calling a method without `()` | `<bound method …>` instead of a result | `zara.best()` |
| `marks = []` written directly under `class` (outside `__init__`) | every object shares one list | Create lists in `__init__` with `self.marks = []` |

## See also

- [05 Dicts and sets](05-dicts-and-sets.md): the dict-based version of a record
- [08 Functions](08-functions.md): methods are functions that belong to a class
- [11 Exceptions](11-exceptions.md): raising from methods
- [06 LLM apps](../ai/06-llm-apps.md): a `MockLLM` class for testing
