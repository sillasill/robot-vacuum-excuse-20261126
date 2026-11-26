"""Robot vacuum's excuse for missing a spot.

Writes one line (at most 120 characters) to /output/entry.txt.
Deterministic, standard library only: no network, no clock, no randomness.
"""

import os

PART_A = "I didn't miss that spot \u2014 the dust bunny living there pays rent now, "
PART_B = "so evicting it would be illegal."


def main() -> None:
    text = PART_A + PART_B
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
