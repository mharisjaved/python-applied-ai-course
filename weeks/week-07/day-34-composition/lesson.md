# Day 34: Class Design and Composition

**Week 7 · Session 34 of 60 · Planned 75 min** · Previous: [Day 33](../day-33-methods/lesson.md) · Next: [Day 35](../day-35-project-inventory/lesson.md)

## Objectives

By the end of this lesson students can:

1. Build a class whose attribute is a **list of other objects** (a `Playlist` that *has* `Song`s) and loop over it.
2. Write methods that search the list and return an object or `None`, checked with `is None`.
3. Design two cooperating classes from a written description: **nouns → classes or attributes, verbs → methods,
   "has a" → a list attribute**, and decide which class is responsible for which job.
4. Test a class with `assert`-based test functions, including error cases with `pytest.raises`.
5. *(Optional preview)* explain the difference between "has-a" (composition) and "is-a" (inheritance).

**Prior knowledge:** classes, methods, validation and `__str__` (Days 32–33), lists of objects (Day 32),
`sorted`/`max` with `key=` (Day 21), `"\n".join` (Day 07), `//` and `%` (Day 03), tests with `assert` and
`pytest.raises` (Day 29).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: write `deposit` from memory | core |
| 0:05–0:20 | Has-a: `Song` and `Playlist` (demo 1–2) | core |
| 0:20–0:27 | Finding and removing: returning `None` (demo 3) | core |
| 0:27–0:37 | Who does what? Designing from a description (demo 4–5) | core |
| 0:37–0:45 | Testing classes (demo 6) | core |
| 0:45–0:48 | Common mistakes (demo 7) | core |
| 0:48–0:70 | Practice exercises 1–4 | core |
| 0:70–0:75 | Recap + exit ticket + Project 04 preview | core |
| +10 min | **Optional** inheritance preview (demo 8) | optional (90-min session) |
| +5 min | Exercise 5 (challenge) started together | optional (90-min session) |

**For 60 min:** do demo 5 (design) as a 3-minute board sketch only and set Exercise 4 as homework.

## 1. Warm-up (5 min)

Students write, on paper, a `deposit(self, amount)` method that raises `ValueError` for amounts of 0 or less.
Check together: `self` parameter, check first then change, `self.balance`. Then ask: "Yesterday each account
was on its own. What real things *contain* other things?" (*A playlist contains songs, a class contains students,
a shop contains products, an order contains items.*)

## 2. Has-a: objects that contain objects (15 min)

**Why:** real programs are rarely one class. A shop has products; a course has students. Instead of one giant
class, we make small classes and let one object **hold** others. This is **composition**, the "has-a" relationship:
*a playlist has songs*.

> **Analogy:** a school bag (the playlist) holds books (songs). The bag knows how many books it has and can find
> one by title; each book knows its own title and page count. You don't ask the bag how many pages a book has:
> you take the book out and ask it.

Live code (demo section 1), one small class first:

```python
class Song:
    def __init__(self, title, artist, seconds):
        self.title = title
        self.artist = artist
        self.seconds = seconds

    def duration(self):
        return f"{self.seconds // 60}:{self.seconds % 60:02d}"   # 215 -> "3:35"

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration()})"
```

`:02d` pads with a zero (`5` → `05`); it's the same format-spec idea as `:.2f` on Day 05.

Then the container (demo section 2):

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []                  # a list that will hold Song objects

    def add(self, song):
        self.songs.append(song)

    def total_seconds(self):
        return sum([song.seconds for song in self.songs])

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for number, song in enumerate(self.songs, start=1):
            lines.append(f"{number}. {song}")        # uses Song.__str__
        return "\n".join(lines)
```

Key points:
- `self.songs` holds **objects**, so `song.seconds` and `song.title` work inside the loop.
- `f"{song}"` calls `Song.__str__`. The playlist does not need to know *how* a song is displayed.

**Prediction question** (demo section 2): after adding `chill_song` to the playlist, we run
`chill_song.seconds = 200`. Does the playlist's total change? (*Yes. The list holds the **same** object, not a copy:
Day 07 name tags again.*)

## 3. Finding and removing: returning `None` (7 min)

Demo section 3 adds:

```python
def find(self, title):
    for song in self.songs:
        if song.title.lower() == title.lower():
            return song
    return None                          # only reached if no song matched

def remove(self, title):
    song = self.find(title)
    if song is None:
        raise ValueError(f"No song called {title} in {self.name}.")
    self.songs.remove(song)
```

- `find` is a *question* method: it returns the object or `None` (Day 17). It does not raise, because "not found"
  is a normal answer when searching.
- `remove` is a *command*: removing something that isn't there is a mistake, so it raises.
- New syntax: **`is None`** is how Python programmers check for `None` (`== None` also works, but `is None` is the
  convention). Use `is` only for `None`; for everything else keep using `==`.
- `remove` reuses `find`: methods calling methods with `self.`.

## 4. Who does what? (4 min)

Demo section 4 has a responsibility table. Ask for each job "which class should do this?":

| Job | Responsible class | Why |
|-----|-------------------|-----|
| format a song's length as `m:ss` | `Song` | it only needs the song's own data |
| total length of the playlist | `Playlist` | it needs all songs |
| find a song by title | `Playlist` | it owns the list |
| check a song's seconds are positive | `Song.__init__` | the object protects its own state |

Rule: **put a method in the class that owns the data it needs.** If `Playlist` starts computing `seconds // 60`
for each song, the job is in the wrong place.

## 5. Designing from a description (6 min)

Show the description in demo section 5 (a gym that runs classes and lets members book places). Underline the
nouns and circle the verbs **with the students**:

| Noun / verb | Decision |
|-------------|----------|
| gym class, member | classes (they have their own data **and** behaviour) |
| name, coach, capacity, membership number | attributes (simple values) |
| book, cancel | methods of the gym class (it owns the list of bookings) |
| "see who is booked", "spaces left" | question methods |
| a gym class **has** members booked | a list attribute: `self.booked = []` |

Then show the **skeleton** in the demo: classes with `__init__` and method headers with docstrings and `pass`. It
runs, but does nothing yet. This is exactly what tomorrow's project starter looks like: design first, fill in
the bodies one by one, test each.

Rule of thumb for "class or attribute?": if it is a single value (a name, a number), it is an attribute. If it has
its own data *and* things it can do, it is a class.

## 6. Testing classes (8 min)

Recap Day 29: a test is a function whose name starts with `test_` and that uses `assert`. For classes, each test
usually **builds a fresh object**, calls a method, then asserts on the state or the return value (demo section 6):

```python
import pytest

def test_total_seconds():
    mix = Playlist("Test")
    mix.add(Song("A", "X", 100))
    mix.add(Song("B", "Y", 50))
    assert mix.total_seconds() == 150

def test_remove_unknown_song_raises():
    mix = Playlist("Test")
    with pytest.raises(ValueError):
        mix.remove("Nothing")
    assert mix.songs == []           # and nothing changed
```

In the notebook we call the test functions ourselves; in a `test_playlist.py` file, `uv run pytest` would find and
run them automatically (Day 29). Each test checks **one behaviour**, including error cases and "nothing changed
after an error".

## 7. Common mistakes (3 min)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `mix.add("Dreams")` (a string, not a `Song`) | later `AttributeError: 'str' object has no attribute 'seconds'` | the playlist expects `Song` objects: `mix.add(Song("Dreams", ...))` |
| `print(mix.songs)` | no error, but shows `[<__main__.Song object at 0x...>, ...]` | a list shows its items with `__repr__`, not `__str__`; loop and print each song (or, as an aside, define `__repr__`) |
| forgetting `self.songs = []` in `__init__` | `AttributeError: 'Playlist' object has no attribute 'songs'` | the list must exist before anything is appended |
| `find` with `return None` inside the loop (as an `else`) | wrong answer: only the first song is ever checked | return `None` **after** the loop has checked every song |

## 8. Optional: inheritance preview (10 min, 90-min session only)

**Clearly optional: not needed for the project, not in the checkpoint.** Composition is "has-a". Inheritance is
"**is-a**": *a savings account is a bank account* with something extra. Demo section 8:

```python
class SavingsAccount(BankAccount):       # SavingsAccount gets everything BankAccount has
    def add_interest(self, percent):
        self.deposit(self.balance * percent / 100)
```

`SavingsAccount("Ken", 200)` uses `BankAccount.__init__`, can `deposit` and `withdraw`, prints with
`BankAccount.__str__`, and *also* has `add_interest`. Message: use inheritance only for true "is-a" relationships;
in this course we prefer composition, and you'll meet inheritance again if you continue with Python.

## 9. Practice (22 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the shelves | the same object in two lists | recall/predict |
| 2 A `Course` of `Student`s | list of objects, search, average, `None` | application |
| 3 Design a library | nouns/verbs → classes/methods, skeleton | design |
| 4 Test the course | test functions, `pytest.raises` | application |
| 5 Build the library (challenge) | three cooperating classes with rules | challenge |

Expected: everyone finishes 1–3, most finish 4, fast students try 5.

Circulate and look for:
- `Course.average()` that reaches into each student's `marks` instead of calling `student.average()`;
- `top_student` that returns the *average* instead of the `Student` object;
- tests that build one shared object at the top and reuse it: one test then changes the result of the next.

## 10. Recap and exit ticket (5 min)

Recap (students supply the sentences):
1. Composition: one object holds other objects in a list attribute ("has-a").
2. Search methods return the object or `None`; check with `is None`. Commands that cannot do their job raise.
3. Put each method in the class that owns the data it needs.
4. Test classes with small test functions: build, act, assert. Use `pytest.raises` for errors.

**Exit ticket:** "A shop sells products; each product has a name, a price and a quantity; the shop can add
products, sell them and list the ones running low." Name the two classes, two attributes of each, and one method
of each.

Answer (example): `Product` (name, price, quantity; `sell`, `restock`) and `Inventory`/`Shop` (products dict or
list; `add_product`, `low_stock`). That is tomorrow's project.

## Homework (25 min)

Finish Exercise 4 and read the [Project 04 brief](../../../projects/04-inventory-manager/README.md). Write down
one question about it for tomorrow.

## Next class

Day 35 is a project day: **Project 04, Inventory Manager**, a multi-file console app with a `Product` class, an
`Inventory` that has many products, a menu and pytest tests. It also starts with Checkpoint 7.

## Instructor notes

- The new syntax today is small (`is None`, `:02d`); the real content is **design thinking**. Spend the time on
  "which class should do this?" questions rather than more syntax.
- If students ask about dicts of objects: yes, exactly like lists. The project stores products in a dict keyed
  by lowercase name, so `find` becomes a single `.get()`.
- Keep inheritance strictly in the optional slot. Do not teach `super()`, overriding `__init__`, `isinstance` or
  multiple inheritance. If a student asks about `super()`, say "that's the next step of inheritance, beyond this
  course".
- `__repr__`: one sentence only, if the list-printing mistake prompts the question.
- Strong students: add `shuffle()` (with `random.seed`) or `sort_by_length()` to `Playlist`. Weaker students: give
  them the finished `Song` class and only ask for `Playlist.add` and `total_seconds`.
