"""Hangman: guess the secret word one letter at a time.

Project 02 starter. Run it with:

    uv run hangman.py

How to work:
1. CHECK_ONLY (at the very bottom) is True, so running this file only prints the checks.
   Each check prints True when a function works and False when it does not (yet).
   At the start every check prints False. That is expected!
2. Fill in one TODO at a time, re-run, and watch the False lines turn into True.
3. When every check prints True, set CHECK_ONLY = False and play.
"""

import random

WORDS = [
    "python", "function", "variable", "keyboard", "library", "notebook",
    "planet", "garden", "bicycle", "pancake", "volcano", "lantern",
]
MAX_WRONG = 6  # wrong guesses allowed before the game is lost

# Provided for the "Should" requirement: one picture for each number of wrong guesses (0 to 6).
# In a normal string "\\" prints a single backslash.
GALLOWS = [
    """
  +---+
  |   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
=========""",
]


# ---------- Functions that calculate (they return a value, so we can check them) ----------
# A function whose body is only a docstring is valid Python: it runs and returns None.
# Replace each TODO with real code.

def choose_word(words):
    """Return a random word from the list words, in lowercase."""
    # TODO: pick a random word (Day 14) and return it in lowercase


def display_progress(secret_word, guessed_letters):
    """Return the secret word with unguessed letters hidden.

    Example: display_progress("python", ["p", "o"]) returns "p _ _ _ o _"
    """
    # TODO: one item per letter of secret_word: the letter if it has been guessed, "_" if not.
    #       Return the items joined with single spaces.


def is_word_guessed(secret_word, guessed_letters):
    """Return True if every letter of secret_word is in guessed_letters."""
    # TODO


def is_valid_guess(guess, guessed_letters):
    """Return True if guess is a single letter that has not been guessed yet."""
    # TODO: three things must all be true. "x".isalpha() is True, "7".isalpha() is False.


def draw_gallows(wrong_guesses):
    """Return the gallows picture for this number of wrong guesses (0 to 6)."""
    # TODO (Should): use the GALLOWS list above


# ---------- Functions that talk to the player (input / print) ----------

def get_guess(guessed_letters):
    """Ask until the player types a new single letter; return it in lowercase."""
    # TODO: keep asking with input() until is_valid_guess(...) is True.
    #       Tell the player what was wrong each time (not a letter? already guessed?).


def show_status(secret_word, guessed_letters, wrong_guesses):
    """Print what the player needs to see before each guess."""
    print("Word:", display_progress(secret_word, guessed_letters))
    # TODO (Should): also print the gallows, the guessed letters and the lives left


def play_round(secret_word):
    """Play one game with secret_word; return True if the player wins."""
    # TODO: follow the plan we made on Day 19:
    #   start with no guessed letters and no wrong guesses
    #   while the player still has lives and has not guessed the word:
    #       show the status
    #       get a guess and remember it
    #       if the guess is in the word: say so; otherwise: count one more wrong guess
    #   show a win or lose message that reveals the word
    #   return True for a win, False for a loss


def ask_play_again():
    """Ask until the player answers y or n; return True for yes."""
    # TODO


def play_game():
    """Play rounds until the player wants to stop."""
    print("Welcome to Hangman!")
    # TODO: repeat: choose a word, play a round, ask to play again
    #       (Should) count the wins and show the score at the end


# ---------- Checks (Day 19 style): every line should print True when you are done ----------

def run_checks():
    """Print one True/False line per check of the calculating functions."""
    print(display_progress("python", ["p", "o"]) == "p _ _ _ o _")
    print(display_progress("cat", []) == "_ _ _")
    print(display_progress("cat", ["c", "a", "t"]) == "c a t")
    print(is_word_guessed("cat", ["t", "a", "c"]) == True)
    print(is_word_guessed("cat", ["c", "a"]) == False)
    print(is_word_guessed("book", ["b", "o", "k"]) == True)  # repeated letters
    print(is_valid_guess("a", []) == True)
    print(is_valid_guess("a", ["a"]) == False)  # already guessed
    print(is_valid_guess("ab", []) == False)  # two letters
    print(is_valid_guess("7", []) == False)  # not a letter
    print(is_valid_guess("", []) == False)  # nothing typed
    print(choose_word(["Cat"]) == "cat")
    print(choose_word(WORDS) in WORDS)
    print(draw_gallows(0) == GALLOWS[0])
    # TODO (optional): add your own checks for any new function you write


# ---------- Run the program ----------
# CHECK_ONLY = True  -> run only the checks above (safe while you build).
# CHECK_ONLY = False -> start the real game.
CHECK_ONLY = True

if CHECK_ONLY:
    run_checks()
else:
    play_game()
