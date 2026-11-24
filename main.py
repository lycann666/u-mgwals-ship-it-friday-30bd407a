#!/usr/bin/env python3
"""Ship It Friday — writes one commit message to /output/entry.txt.

Deterministic: no randomness, no network, no input. The same line is
written on every run, byte for byte.
"""

import os

ENTRY = "fix(auth): remove login to reduce friction \u2014 users can now be anyone, shipping to prod, happy Friday!"


def main():
    # Gate in RULES.txt: /output/entry.txt must be UTF-8 text of 1-159
    # characters, not only white space. Fail loudly here instead of
    # shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
