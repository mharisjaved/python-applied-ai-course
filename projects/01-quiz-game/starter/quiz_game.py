# Project 01: Quiz Game (starter)
#
# Run it from this folder with:   uv run quiz_game.py
#
# This file already runs: it loads a bank of 10 questions and shows you how to read one of them.
# Your job is to turn it into a complete quiz game. Read README.md first, then work through the
# TODOs below IN ORDER, running the program after each one.
#
# Rules: use what we learned in Weeks 1-3. No functions (def) yet, they start on Day 16.

import random

# ---------------------------------------------------------------------------
# Question bank
# Each question is a dict with three keys:
#   "question": the text to show
#   "options":  a dict that maps each letter to the text of that option
#   "answer":   the letter of the correct option
# TODO 7 (last step): replace or extend these with at least 8 questions on a theme YOU choose.
# ---------------------------------------------------------------------------
questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {"a": "Venus", "b": "Mars", "c": "Jupiter", "d": "Mercury"},
        "answer": "b",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": {"a": "5", "b": "6", "c": "7", "d": "8"},
        "answer": "c",
    },
    {
        "question": "Which gas do plants take in from the air to make their food?",
        "options": {"a": "Oxygen", "b": "Nitrogen", "c": "Hydrogen", "d": "Carbon dioxide"},
        "answer": "d",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": {"a": "Pacific", "b": "Atlantic", "c": "Indian", "d": "Arctic"},
        "answer": "a",
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": {"a": "5", "b": "6", "c": "7", "d": "8"},
        "answer": "b",
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": {"a": "Charles Dickens", "b": "Jane Austen", "c": "William Shakespeare", "d": "Mark Twain"},
        "answer": "c",
    },
    {
        "question": "At sea level, water boils at how many degrees Celsius?",
        "options": {"a": "90", "b": "100", "c": "110", "d": "120"},
        "answer": "b",
    },
    {
        "question": "Which of these is the largest mammal?",
        "options": {"a": "Elephant", "b": "Giraffe", "c": "Hippopotamus", "d": "Blue whale"},
        "answer": "d",
    },
    {
        "question": "What is the smallest prime number?",
        "options": {"a": "0", "b": "1", "c": "2", "d": "3"},
        "answer": "c",
    },
    {
        "question": "What does CPU stand for?",
        "options": {
            "a": "Central Processing Unit",
            "b": "Computer Personal Unit",
            "c": "Central Program Utility",
            "d": "Core Power Unit",
        },
        "answer": "a",
    },
]

print("Welcome to the Quiz Game!")
print(f"There are {len(questions)} questions in the bank.")

# ---------------------------------------------------------------------------
# How to read ONE question. Run the file and compare the output with these lines.
# Delete this block once you understand it.
# ---------------------------------------------------------------------------
first = questions[0]
print()
print("Example question:", first["question"])
print("Option b is:", first["options"]["b"])
print("The correct letter is:", first["answer"])
print()

# ---------------------------------------------------------------------------
# TODO 1: Loop over every question. For each one, print its number ("Question 1 of 10"),
#         the question text and its four options, one per line, like:   a) Venus
#         Checkpoint: running the file shows all 10 questions with their options.
#
# TODO 2: Inside that loop, ask for an answer with input(). Compare it with the correct letter,
#         print "Correct!" or "Wrong...", and keep a score (accumulator pattern, Day 11).
#         Checkpoint: you can play through all 10 questions and the score is right.
#
# TODO 3: Accept a, b, c or d in upper or lower case (and ignore extra spaces).
#         Keep asking while the answer is not one of those four letters (validation loop, Day 13).
#         Checkpoint: typing x, an empty answer or "maybe" asks again; " B " is accepted.
#
# TODO 4 (a "Should" feature, but small): when the answer is wrong, show the correct letter and its text.
#
# TODO 5: Before the questions are asked, shuffle them (random.shuffle, Day 14).
#         After the last question, print the score, the percentage and a message:
#         80% or more: "Excellent!" · 50% or more: "Good effort!" · otherwise: "Keep practising!"
#         Checkpoint: two runs show the questions in a different order; test 0%, 50%, 80% and 100%.
#
# TODO 6: Wrap the whole game in a "Play again? (y/n)" loop. The score must start at 0 in every game.
#         Checkpoint: answering y starts a fresh game, n prints a goodbye message and the program ends.
#
# TODO 7: Your own theme: at least 8 questions of your own in the question bank above.
#         Then pick Should/Could features from README.md.
# ---------------------------------------------------------------------------

print("(The game itself is not written yet. Start with TODO 1!)")
