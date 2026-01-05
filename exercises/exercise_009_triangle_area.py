# ============================================================
#            EXERCISE 009 — TRIANGLE AREA
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise:
#   Calculate the area of a triangle using Heron's formula.
#   Use helper functions to keep the logic simple.
#
# History:
#   Heron (Hero) of Alexandria was a Greek mathematician and engineer
#   who lived in the 1st century CE. He is known for Heron's formula,
#   which finds a triangle's area from its side lengths.
# ============================================================


print("\n# -----------------------------")
print("# Triangle area (Heron's formula)")
print("# -----------------------------\n")


# A triangle is valid if every side is shorter than the sum of the other two.
def valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
    


# Half of the perimeter (used by Heron's formula).
def half_perimeter(a, b, c):
    return (a + b + c) / 2


# Area calculation using Heron's formula.
def triangle_area(a, b, c):
    if not valid_triangle(a, b, c):
        return None
    s = half_perimeter(a, b, c)
    # A = sqrt(s(s - a)(s - b)(s - c))
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


# Test cases
print(triangle_area(3.0, 4.0, 5.0)) # Expected: 6.0
