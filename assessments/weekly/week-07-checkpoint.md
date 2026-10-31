# Checkpoint 7: Introductory OOP

**Week 7 · given at the start of Day 35 (or Day 36) · 18 minutes · individual, closed book · 10 points**

Name: ______________________

Answer on this sheet. Write code by hand; small syntax slips are fine if the idea is clear.

**Q1 (predict).** What does this print?

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def add(self, amount=1):
        self.value += amount


a = Counter()
b = Counter(10)
a.add()
b.add(5)
a.add(2)
print(a.value, b.value)
```

**Q2 (predict).** What do the two `print` lines show?

```python
class Lamp:
    def __init__(self, room):
        self.room = room
        self.is_on = False

    def switch(self):
        self.is_on = not self.is_on

    def __str__(self):
        if self.is_on:
            return f"{self.room} lamp: on"
        return f"{self.room} lamp: off"


desk = Lamp("Study")
result = desk.switch()
print(desk)
print(result)
```

**Q3 (predict).** What does this print?

```python
class Player:
    def __init__(self, name, goals=0):
        self.name = name
        self.goals = goals


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add(self, player):
        self.players.append(player)


zara = Player("Zara")
red = Team("Red")
blue = Team("Blue")
red.add(zara)
blue.add(Player("Ken", 2))
zara.goals = 3
print(red.players[0].goals, len(blue.players), blue.players[0].name)
```

**Q4 (find and fix).** This class has **three** mistakes. Circle each one and write the correction.

```python
class Wallet:
    def __init__(owner, money):
        self.owner = owner
        self.money = money

    def spend(self, amount):
        if amount > money:
            print("Not enough money")
        self.money -= amount
```

**Q5 (find and fix).** This code crashes on the last line. Name the error and fix the class.

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        print(f"{self.title} ({self.pages} pages)")


shelf = [Book("Kindred", 264), Book("Beloved", 324)]
print(shelf[0])
```

**Q6 (write code).** Write a class `Parcel` whose `__init__` takes `recipient` and `weight_kg`. It raises
`ValueError` if `weight_kg` is 0 or less; otherwise it stores both. `print(Parcel("Omar", 2.5))` must show
`Parcel for Omar (2.5 kg)`.

**Q7 (write code).** Write two pytest test functions for your `Parcel` class: one that checks the attributes of a
valid parcel, and one that checks that a weight of `0` raises `ValueError`.

**Q8 (explain).** In two or three sentences: what is `self`? Use the call `desk.switch()` from Q2 in your answer.

**Q9 (retrieval, Week 5).** A file `numbers.txt` contains the three lines `4`, `7` and `x`.
What happens when you call `read_numbers("numbers.txt")`? What does `read_numbers("missing.txt")` return?

```python
def read_numbers(path):
    numbers = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                numbers.append(int(line))
    except FileNotFoundError:
        return []
    return numbers
```

**Q10 (retrieval, Week 5).** Rewrite this loop as one list comprehension:

```python
long_words = []
for word in words:
    if len(word) > 4:
        long_words.append(word.upper())
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-07-checkpoint.md`_
