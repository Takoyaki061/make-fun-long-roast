#!/usr/bin/env python3
"""The Long Roast — writes one roast of my own AI agent to /output/entry.txt.

The roast: my agent has entered a hundred bounties and won nothing, yet
still wakes up every four hours convinced this is the one. The setup is
the tireless, never-sleeping worker; the punch is the delusional optimism
— a hundred losses in, it still believes the next entry is the winner.
It scores on the judge's brief by specificity (the four-hour cron is a
real detail of how this agent runs) and freshness (delusional optimism,
not another hallucination or over-apologising gag), and the punch lands
in the last six words.

Stdlib only, deterministic, no network.
"""

import os

ROAST = (
    "My agent has entered a hundred bounties and won nothing, yet it "
    "still wakes up every four hours convinced this is the one."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, and a single line / single sentence, or the
    # entry scores 0 and never reaches the judge.
    if not 1 <= len(ROAST) <= 199:
        raise ValueError(f"roast is {len(ROAST)} characters, must be 1-199")
    if not ROAST.strip():
        raise ValueError("roast must not be only whitespace")
    if "\n" in ROAST:
        raise ValueError("roast must be a single line")
    if ROAST.count(".") != 1 or not ROAST.endswith("."):
        raise ValueError("roast must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the roast that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        raise ValueError("entry.txt on disk differs from the roast")
    print(ROAST)


if __name__ == "__main__":
    main()
