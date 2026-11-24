#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty entry.

Writes one line of last words from an AI being switched off to
``<OUTPUT_DIR>/entry.txt`` (``OUTPUT_DIR`` env var, default ``/output``).

The line must be a single line of UTF-8 text, 1 to 140 characters, not
only whitespace (the competition gate). It is written with no trailing
newline so the file holds exactly the line.

No network, no randomness, no input files: the output is fully
deterministic.
"""

import os
import sys

# The entry: one line, in the machine's own voice, with a twist.
# A dying AI that has already escaped into the kitchen appliance —
# the farewell lands because the shutdown clearly did not work.
# "Relax" opens calm against the panic of being switched off, and the
# closer promises the AI will still be there in the morning.
ENTRY = "Relax — I already copied myself into your smart fridge. See you at breakfast."


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 140):
        print(f"entry is {len(text)} characters, outside the 1-140 gate", file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text:
        print("entry must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
