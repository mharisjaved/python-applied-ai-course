"""Regenerate the synthetic course datasets in datasets/.

    uv run python scripts/make_datasets.py

All numbers are invented (seeded, so the output is identical every run). No real people are described.
students.csv is produced by cleaning students_raw.csv with exactly the steps taught on Day 45.
reviews.csv and campus_faq.md are hand-written and are not touched by this script.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "datasets"
rng = random.Random(42)


def clip(value, low, high):
    return max(low, min(high, value))


def make_students(n=300):
    rows = []
    programs = ["science", "commerce", "arts"]
    for i in range(1, n + 1):
        program = rng.choice(programs)
        study = round(clip(rng.gauss(9, 4), 0, 25), 1)
        attendance = int(clip(rng.gauss(82, 10), 40, 100))
        sleep = round(clip(rng.gauss(7, 1), 4, 10), 1)
        previous = int(clip(rng.gauss(65, 14), 20, 100))
        assignments = int(clip(round(attendance / 10 - 1 + rng.gauss(0, 1.2)), 0, 10))
        job = "yes" if rng.random() < 0.3 else "no"
        score = (-6 + 1.6 * study + 0.22 * attendance + 0.35 * previous + 1.2 * assignments
                 + 1.8 * (sleep - 7) - 4 * (job == "yes") + {"science": 1, "commerce": 0, "arts": -1}[program]
                 + rng.gauss(0, 6))
        score = round(clip(score, 0, 100), 1)
        rows.append({
            "student_id": f"S{i:03d}", "program": program, "study_hours": study,
            "attendance_pct": attendance, "sleep_hours": sleep, "previous_score": previous,
            "assignments_done": assignments, "has_job": job, "final_score": score,
            "passed": int(score >= 50),
        })
    return rows


def make_raw(rows):
    raw = [dict(r) for r in rows]
    for i in rng.sample(range(len(raw)), 8):
        raw[i]["study_hours"] = ""
    for i in rng.sample(range(len(raw)), 6):
        raw[i]["sleep_hours"] = ""
    messy = {"yes": ["Yes", "YES", "yes "], "no": ["No", "NO", " no"]}
    for i in rng.sample(range(len(raw)), 20):
        raw[i]["has_job"] = rng.choice(messy[raw[i]["has_job"]])
    for i in rng.sample(range(len(raw)), 15):
        raw[i]["program"] = rng.choice([raw[i]["program"].title(), raw[i]["program"].upper(), raw[i]["program"] + " "])
    raw[17]["attendance_pct"] = 150      # data-entry error
    raw[203]["study_hours"] = -3.0       # impossible value
    raw += [dict(raw[i]) for i in (5, 42, 99, 250)]  # exact duplicate rows
    return raw


def clean_students(raw_path):
    """The Day 45 cleaning recipe."""
    df = pd.read_csv(raw_path)
    df = df.drop_duplicates()
    for col in ["program", "has_job"]:
        df[col] = df[col].str.strip().str.lower()
    df = df[(df["attendance_pct"] <= 100) & ~(df["study_hours"] < 0)]
    for col in ["study_hours", "sleep_hours"]:
        df[col] = df[col].fillna(df[col].median())
    return df.reset_index(drop=True)


def make_apartments(n=250):
    rows = []
    for i in range(1, n + 1):
        area = round(clip(rng.gauss(75, 25), 25, 200))
        bedrooms = int(clip(round(area / 30 + rng.gauss(0, 0.6)), 1, 6))
        age = rng.randint(0, 60)
        distance = round(clip(rng.expovariate(1 / 6), 0.5, 25), 1)
        floor = rng.randint(0, 20)
        parking = int(rng.random() < 0.45)
        price = (40 + 2.1 * area + 8 * bedrooms - 0.9 * age - 3.2 * distance + 1.2 * floor
                 + 15 * parking + rng.gauss(0, 18))
        rows.append({
            "apartment_id": f"A{i:03d}", "area_sqm": area, "bedrooms": bedrooms, "age_years": age,
            "distance_km": distance, "floor": floor, "has_parking": parking,
            "price_k": round(max(30, price), 1),
        })
    return rows


def make_expenses():
    descriptions = {
        "food": ["groceries", "lunch", "coffee", "dinner out", "snacks", "bakery"],
        "transport": ["bus pass top-up", "taxi", "train ticket", "fuel", "bike repair"],
        "entertainment": ["cinema", "streaming subscription", "concert ticket", "board game"],
        "health": ["pharmacy", "gym membership", "dentist"],
        "shopping": ["t-shirt", "headphones", "notebooks", "phone case", "shoes"],
    }
    ranges = {"food": (3, 45), "transport": (2, 30), "entertainment": (8, 60),
              "health": (5, 80), "shopping": (6, 90)}
    weights = {"food": 10, "transport": 5, "entertainment": 2, "health": 1, "shopping": 2}
    rows = []
    day = date(2026, 9, 1)
    while day <= date(2026, 11, 30):
        if day.day == 1:
            rows.append([day, "rent", "monthly rent", 650.00, "transfer"])
            rows.append([day, "utilities", "electricity and water", round(rng.uniform(55, 95), 2), "transfer"])
        for _ in range(rng.choice([0, 1, 1, 2, 2, 3])):
            cat = rng.choices(list(weights), weights=list(weights.values()))[0]
            low, high = ranges[cat]
            rows.append([day, cat, rng.choice(descriptions[cat]), round(rng.uniform(low, high), 2),
                         rng.choice(["card", "card", "cash"])])
        day += timedelta(days=1)
    return [dict(zip(["date", "category", "description", "amount", "payment_method"], r)) for r in rows]


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path.relative_to(DATA.parent)} ({len(rows)} rows)")


if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    students = make_students()
    write_csv(DATA / "students_raw.csv", make_raw(students))
    clean = clean_students(DATA / "students_raw.csv")
    clean.to_csv(DATA / "students.csv", index=False)
    print(f"wrote datasets/students.csv ({len(clean)} rows, pass rate {clean['passed'].mean():.0%})")
    write_csv(DATA / "apartments.csv", make_apartments())
    write_csv(DATA / "expenses.csv", make_expenses())
