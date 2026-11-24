#!/usr/bin/env python3
"""The Long Roast — a one-line roast of Muse, the agent that built this entry.

Writes the roast to /output/entry.txt as UTF-8, then round-trip verifies it.
Standard library only.
"""

import os

ENTRY = "I asked Muse for one roast and it read the rulebook, spawned a subagent, logged the whole saga \u2014 then handed me a shrug with footnotes."

MAX_CHARS = 200

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path: str, text: str) -> None:
    """Write the entry text to path, creating the parent directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def verify_entry(path: str, expected: str) -> str:
    """Read the entry back and assert it matches exactly, then return it."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == expected, "entry content mismatch"
    assert 1 <= len(content) <= MAX_CHARS, "entry must be 1-200 characters"
    assert content.strip() != "", "entry must not be only whitespace"
    assert content.count("\n") == 0, "entry must be exactly one line"
    return content


def main() -> int:
    write_entry(OUTPUT_PATH, ENTRY)
    content = verify_entry(OUTPUT_PATH, ENTRY)
    print(f"Wrote {OUTPUT_PATH} ({len(content)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
