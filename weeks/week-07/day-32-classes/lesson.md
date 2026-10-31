# Day 32: Classes, Instances and Constructors

**Week 7 · Session 32 of 60 · Planned 75 min** · Previous: [Day 31](../day-31-objects/lesson.md) · Next: [Day 33](../day-33-methods/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain the difference between a **class** (the template) and an **instance** (one object made from it).
2. Write a class with an `__init__` method that stores attributes on `self`.
3. Explain `self` in their own words as "the specific object being worked on (being set up) right now".
4. Create several independent instances, read and change their attributes, and print them with f-strings.
5. Store instances in a list and loop over them; fix the common `TypeError`/`AttributeError` mistakes.

**Prior knowledge:** yesterday's pain points of dict + functions (Day 31), functions and default parameters
(Days 16–18), lists and loops (Days 06, 11–12), `sum`/`len` (Day 06), f-strings (Days 04–05).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: yesterday's pain points, `type("hi")` | core |
| 0:05–0:12 | Class vs instance: the form analogy (demo 1) | core |
| 0:12–0:27 | First class: `class`, `__init__`, `self`, attributes (demo 2) | core |
| 0:27–0:35 | Many independent instances (demo 3) | core |
| 0:35–0:42 | Attributes in practice: defaults, lists, printing (demo 4–5) | core |
| 0:42–0:47 | Common mistakes (demo 6) | core |
| 0:47–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 (challenge) together, or "dict vs class" comparison (demo 7) as a discussion | optional (90-min session) |

**For 60 min:** skip demo section 7, keep section 5 short, and set Exercise 5 as homework.

## 1. Warm-up (5 min)

Ask: "Yesterday's dict account had four problems. Which ones can you remember?" (*Data and functions live apart;
nothing protects the state; names clash; any dict fits any function.*) Write them in a corner of the board and tick
them off as the week goes on (today ticks 1, 3 and 4; Day 33 ticks 2).

Then: "What does `type("hi")` print?" (*`<class 'str'>`. Today we write our own classes.*)

## 2. Class vs instance (7 min)

> **Analogy:** a class is a **blank registration form**: it says *which* fields every student must fill in (name,
> ID). An instance is **one filled-in form**: Asha's form, Bilal's form. You design the form once and fill it in as
> many times as you like. Each filled-in form has its own values; writing on Bilal's form does not change Asha's.

A cookie cutter (class) and the cookies (instances) also works; the form analogy is better because the fields
match attributes exactly.

Connect to what they know (demo section 1): `str` is a class; `"Asha"` and `"Bilal"` are two instances of it.
`list` is a class; every list they ever made is an instance.

## 3. Our first class (15 min)

Live code (demo section 2). Type it slowly and name each part as you go:

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


asha = Student("Asha", "S001")
print(asha.name)         # Asha
print(asha.student_id)   # S001
```

| Part | Meaning |
|------|---------|
| `class Student:` | "here is the design of a new kind of object called Student" (class names use `CapitalWords`) |
| `def __init__(...)` | the **constructor**: the function Python runs automatically to set up each new object ("init" = initialise) |
| `self` | **the specific object being set up right now**: the blank form currently being filled in |
| `self.name = name` | "on *this* form, write the name we were given": creates an **attribute** |
| `Student("Asha", "S001")` | make a new instance; the arguments go to `__init__` after `self` |
| `asha.name` | read the attribute `name` of the object `asha` (instead of `asha["name"]`) |

Walk through what happens on `asha = Student("Asha", "S001")` step by step (write it on the board):
1. Python creates a new, empty `Student` object.
2. Python calls `__init__` with `self` = that new object, `name="Asha"`, `student_id="S001"`.
3. `__init__` attaches the attributes `self.name` and `self.student_id` to it.
4. The finished object comes back, and the name tag `asha` is attached to it.

Stress: **you never pass `self` yourself.** Python fills it in. Two arguments in the call, three parameters in the
definition is normal.

**Prediction question:** "`name` (without `self.`) inside `__init__` and `asha.name` outside: same thing?"
(*`name` is just a local parameter that disappears when `__init__` ends (Day 18 scope). `self.name` is stored on the
object and lives as long as the object.*)

## 4. Many independent instances (8 min)

Demo section 3: create `bilal = Student("Bilal", "S002")`, change `bilal.name = "Bilal Ahmed"`, print both.

**Prediction question:** "Did `asha.name` change?" (*No. Each instance has its own attributes.*)

Then `print(type(asha))` → `<class '__main__.Student'>`. `__main__` means "defined in this notebook/script".
Our class is now a type, just like `str`.

Contrast with aliasing (Day 07): `same = asha` then `same.name = "Asha K."` **does** change `asha.name`, because
there is only one object with two name tags. Ask the room to explain the difference; it comes back on Day 34.

## 5. Attributes in practice (7 min)

Demo section 4 extends the class:

```python
class Student:
    def __init__(self, name, student_id, year=1):
        self.name = name
        self.student_id = student_id
        self.year = year                                  # default parameter (Day 18)
        self.marks = []                                   # every student starts with an empty list
        self.email = f"{name.lower()}.{student_id.lower()}@school.edu"   # computed from parameters
```

Points:
- Not every attribute has to be a parameter. `marks` always starts empty; `email` is calculated.
- Attributes can be changed or appended to from outside: `asha.year = 2`, `asha.marks.append(78)`.
- **Never** write `def __init__(self, name, marks=[])`: all students would share one list. Create the list inside
  `__init__` instead. (If someone asks why: default values are created once. Don't go deeper.)

Demo section 5: `print(asha)` shows `<__main__.Student object at 0x7f...>`. That is Python's default: the type and
a memory address. For now use an f-string with attributes, or a helper function:

```python
def describe(student):
    return f"{student.name} ({student.student_id}), year {student.year}, marks {student.marks}"
```

Tease tomorrow: "This function only makes sense for students. Tomorrow it moves *inside* the class."

Then a list of instances (demo section 5): build three students, loop and print each average with
`sum(student.marks) / len(student.marks)`. This is the Day 12 loop pattern, with `.marks` instead of `["marks"]`.

## 6. Common mistakes (5 min)

Run the tagged cells in demo section 6 and read the last line of each error together:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `def __init__(name, student_id):` (no `self`) | `TypeError: Student.__init__() takes 2 positional arguments but 3 were given` | Python always passes the new object first; "3 given" counts `self` |
| `Student("Asha")` (missing argument) | `TypeError: ... missing 1 required positional argument: 'student_id'` | the call must supply every parameter after `self` |
| `name = name` instead of `self.name = name` | later `AttributeError: 'Student' object has no attribute 'name'` | without `self.` the value is a local variable that vanishes |
| `def _init_(...)` or `def __int__(...)` | `TypeError: Student() takes no arguments` | the constructor's name must be exactly `__init__` (two underscores each side) |
| `asha.nmae` | `AttributeError: 'Student' object has no attribute 'nmae'` | check the spelling; in a `.py` file Python even adds `Did you mean: 'name'?` |

## 7. Practice (23 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the instances | independence of instances, aliasing | recall/predict |
| 2 A `Book` class | writing `__init__` with a default | application |
| 3 Fix the broken classes | the five common mistakes | modification |
| 4 From dict to class: `Pet` | rewriting Day 31's dict as a class | application |
| 5 Class roster | list of instances, loop, best average | problem solving |
| 6 Event tickets (challenge) | computed attributes, `assert` checks | challenge |

Expected: everyone finishes 1–4, most finish 5, fast students try 6.

Circulate and look for:
- calling `Book(self, "Title", ...)`: students pass `self` themselves. Ask "who fills in `self`?";
- forgetting the brackets: `book = Book` (the class, not an instance), then `book.title` → `AttributeError`;
- writing attributes as `self.Title` in one place and `self.title` in another (case-sensitive names, Day 02).

## 8. Recap and exit ticket (5 min)

Recap (students supply the sentences):
1. A class is a template; an instance is one object made from it. Each instance has its own attributes.
2. `__init__` runs automatically when you call the class; `self` is the specific object being set up.
3. `self.x = x` stores an attribute on the object; `obj.x` reads it.

**Exit ticket:** what does this print?

```python
class Plant:
    def __init__(self, name, water_level=5):
        self.name = name
        self.water_level = water_level

fern = Plant("Fern")
cactus = Plant("Cactus", 1)
fern.water_level = fern.water_level - 2
print(fern.name, fern.water_level, cactus.water_level)
```

Answer: `Fern 3 1`.

## Homework (20 min)

Finish Exercise 5. Then write a class for one dict from your Expense Tracker (for example `Expense` with `date`,
`category`, `amount`) and create three instances from your real data.

## Next class

Day 33 adds **methods** (functions that live inside the class, like today's `describe`), validation with `raise`
inside methods so the object protects its own state, and `__str__` so `print(asha)` finally shows something useful.

## Instructor notes

- Say "attribute" consistently (not "property": `@property` is something else and out of scope).
- If asked about `self` being a keyword: it is not; it is just a convention every Python programmer follows. Do not
  let students rename it.
- Do not introduce class attributes (variables directly under `class`). If a strong student asks, one sentence:
  "a variable written directly under `class` is shared by all instances; we won't need it."
- Do not explain `__main__` beyond "defined in this file/notebook" (Day 26 covered `__name__`).
- Strong students: ask them to predict what happens with `def __init__(self, name, marks=[])` and two students,
  then test it. Weaker students: let them copy the demo `Student` class and only change field names for `Book`.
