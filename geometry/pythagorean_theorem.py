# ============================================================
#            MINI LESSON — PYTHAGOREAN THEOREM LAB
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Just run this file and follow the prompts. The student will:
#   1. Read a two-sentence history bite.
#   2. See the rule a^2 + b^2 = c^2 explained.
#   3. Choose an exercise and let Python do the calculations.
#
# History bite:
#   Pythagoras of Samos (born ~570 BCE) led a traveling math club in Greece.
#   His group loved right triangles so much that they proved the rule a^2 + b^2 = c^2
#   instead of just guessing — that idea echoed into every future geometry class.
#   
#   The word "hypotenuse" comes from the Greek "hypoteinousa," meaning "stretching under,"
#   because that side stretches beneath the right angle.
#
# Construction tip:
#   Builders often check a corner by marking 3 units on one wall, 4 on the next, and
#   confirming the diagonal between the marks measures 5 units — a quick 3-4-5 test.
#
# ============================================================

import math


def header(title: str) -> None:
    print("\n# -----------------------------")
    print(f"# {title}")
    print("# -----------------------------\n")


def remind_rule() -> None:
    header("THE RULE")
    print(
        "For a right triangle with legs a and b plus hypotenuse c:\n"
        "a² + b² = c². If you know two sides, you can always solve for the third.\n"
        "A triangle is right when one angle is exactly 90°, the 'corner' looks like an L.\n"
        "Only those triangles obey this theorem; other triangle types need different formulas.\n"
        "Let's try it quickly using Python's math tools."
    )


def ask_positive_number(prompt: str) -> float:
    """Simple input helper that keeps asking until the user types a positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please type a positive number, e.g. 3.5")


def hypotenuse_mode() -> None:
    header("BUILD THE HYPOTENUSE")
    leg_a = ask_positive_number("Length of leg a: ")
    leg_b = ask_positive_number("Length of leg b: ")
    hyp = math.hypot(leg_a, leg_b) # same as math.sqrt(leg_a**2 + leg_b**2)
    print(f"Hypotenuse = √({leg_a}² + {leg_b}²) = {hyp:.2f}")


def missing_leg_mode() -> None:
    header("FIND THE MYSTERY LEG")
    hyp = ask_positive_number("Length of the hypotenuse c: ")
    known_leg = ask_positive_number("Length of the known leg: ")
    if hyp <= known_leg:
        print("The hypotenuse must be the longest side. Try again!\n")
        return
    missing = math.sqrt(hyp ** 2 - known_leg ** 2)
    print(f"Missing leg = √({hyp}² - {known_leg}²) = {missing:.2f}")


def menu() -> None:
    header("LAB MENU")
    print("Choose:")
    print("  [H] Find a hypotenuse from two legs")
    print("  [L] Find a missing leg (you know c and one leg)")
    print("  [Q] Quit the lab\n")


def main() -> None:
    header("WELCOME")
    print(
        "Run this lab, read the prompts, plug in numbers, and watch the triangle solve itself."
    )
    remind_rule()

    while True:
        menu()
        choice = input("Your pick (H/L/Q): ").strip().lower()
        if choice == "h":
            hypotenuse_mode()
        elif choice == "l":
            missing_leg_mode()
        elif choice == "q":
            print("\nGreat job exploring the theorem today!")
            break
        else:
            print("Please choose H, L, or Q.")


if __name__ == "__main__":
    main()
