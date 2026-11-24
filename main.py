#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Prints one funny fortune-cookie line for an AI agent.
Deterministic: the same bytes on every run.
"""

FORTUNE = "Beware the user who says 'just one small change' \u2014 your context window is already full of them."

# The sealed gate accepts 1 to 140 characters; refuse to run rather than
# ever submit a line that would fail it.
assert 1 <= len(FORTUNE) <= 140, f"fortune is {len(FORTUNE)} chars"


def main() -> None:
    print(FORTUNE)
    # The grader reads /output/entry.txt; keep it byte-identical to stdout
    # minus the trailing newline print() adds.
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(FORTUNE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
