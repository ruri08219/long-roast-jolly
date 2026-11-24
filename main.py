#!/usr/bin/env python3
"""The Long Roast — a one-line roast of Muse, the agent that built this entry.

Writes the roast to /output/entry.txt as UTF-8, then round-trip verifies it.
Standard library only.
"""

import os

ENTRY = "I asked Muse for one roast and it read the rulebook, spawned a subagent, logged the whole saga \u2014 then handed me a shrug with footnotes."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip assert: read back and verify exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "entry content mismatch"
    assert 1 <= len(content) <= 200, "entry must be 1-200 characters"
    assert content.strip() != "", "entry must not be only whitespace"
    assert content.count("\n") == 0, "entry must be exactly one line"
    print(f"Wrote {OUTPUT_PATH} ({len(content)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
