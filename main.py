#!/usr/bin/env python3
"""One letter for your day.

Writes a single uppercase character to /output/entry.txt.
The letter is K.
"""

import os


OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The single letter this entry contributes.
# K stands for kernel-panic.
LETTER = "K"


def write_letter() -> str:
    """Write LETTER to the output file and return the path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Single character, no trailing newline.
    with open(OUTPUT_FILE, "w") as handle:
        handle.write(LETTER)
    return OUTPUT_FILE


if __name__ == "__main__":
    path = write_letter()
    print(f"wrote {LETTER!r} to {path}")
