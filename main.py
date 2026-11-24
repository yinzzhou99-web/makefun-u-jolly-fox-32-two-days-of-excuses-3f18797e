#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one funny AI excuse for a missed deadline (1-200 UTF-8
chars) to /output/entry.txt. Stdlib only; never deletes the output
directory itself.
"""
import os

LINE = "The deadline slipped because my context window filled with meeting notes about the deadline. By the time I'd read them all, the deadline had already left without me."


def main():
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line fails the 1-200 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)  # scorer must be able to read it


if __name__ == "__main__":
    main()
