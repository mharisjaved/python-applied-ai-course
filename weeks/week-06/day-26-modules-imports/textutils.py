"""textutils: small helpers for working with text (Day 26 example module).

Use it from a notebook or another .py file in the same folder:

    import textutils
    textutils.word_count("Hello there, Asha!")

Run it directly to see its self-checks:

    uv run textutils.py
"""

from collections import Counter

PUNCTUATION = ".,!?;:\"'()"


def clean_words(text):
    """Return the words in text, lowercased and without punctuation around them."""
    words = []
    for word in text.lower().split():
        word = word.strip(PUNCTUATION)
        if word != "":
            words.append(word)
    return words


def word_count(text):
    """Return how many words text contains."""
    return len(clean_words(text))


def top_words(text, n=3):
    """Return the n most common words as a list of (word, count) tuples."""
    return Counter(clean_words(text)).most_common(n)


def initials(full_name):
    """Return the initials of a name, e.g. "asha khan" -> "A.K."."""
    return "".join([part[0].upper() + "." for part in full_name.split()])


if __name__ == "__main__":
    # This block runs only when the file is run directly (uv run textutils.py).
    # It does NOT run when a notebook or another file imports textutils.
    print("Self-checks for textutils:")
    print(clean_words("Hello, hello WORLD!") == ["hello", "hello", "world"])
    print(word_count("The cat sat on the mat.") == 6)
    print(top_words("tea coffee tea juice tea coffee", 2) == [("tea", 3), ("coffee", 2)])
    print(initials("asha khan") == "A.K.")
