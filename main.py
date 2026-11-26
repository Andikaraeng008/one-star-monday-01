#!/usr/bin/env python3
"""One Star for Monday: write the one-star review to /output/entry.txt."""
import os

REVIEW = "One star. Monday took my Sunday leftovers, reheated them as a 7 a.m. meeting, and tipped itself with my sleep."
# Gate: 20 words, 110 characters, single line of plain text.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)

if __name__ == "__main__":
    main()
