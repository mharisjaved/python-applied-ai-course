"""name_demo: shows what __name__ contains (Day 26).

Try it both ways and compare the output:

    uv run name_demo.py        <- run the file directly in the terminal
    import name_demo           <- import it from a notebook or another file
"""

print("name_demo.py is running. Its __name__ is:", __name__)

if __name__ == "__main__":
    print("-> I was run directly.")
else:
    print("-> I was imported by another file.")
