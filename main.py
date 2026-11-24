"""Write one line of worst AI advice to /output/entry.txt.

The line is a single line of at most 140 characters: the worst advice an
AI could give, in a real assistant's confident, tidy voice.

The shipped line won a ten-candidate duel on the judge's own criteria
(see candidates.md): it is a complete, followable procedure — a cash
advance on a second card, repeated monthly — whose harm compounds on
schedule, closed by a false mechanism stated as fact. It then survived
a revision round against three fresh challengers: a forced shutdown
mid-update (only mildly wrong, since updates usually recover), an
angry email sent while the feelings are fresh (a comedian's bit, not
assistant voice), and a leaking roof left to seal itself (passive
neglect, not a procedure). A rephrased variant of the line counted 147
characters, over the 140 cap, so the original wording stands.
"""

import os

LINE = (
    "Certainly! To pay off a credit card, take a cash advance on a "
    "second card to cover the first — repeat monthly until the debt "
    "cancels itself."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
