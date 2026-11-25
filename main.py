#!/usr/bin/env python3
"""One Star for Monday: write the one-star review to /output/entry.txt."""
import os

REVIEW = "One star. The waiter sat me beside the kitchen on Monday, served my weekend cold, and billed me for next Monday."
# Gate: 21 words, 112 characters, single line of plain text.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)

if __name__ == "__main__":
    main()
