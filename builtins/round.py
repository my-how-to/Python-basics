# ============================================================
#                    BUILT-IN FUNCTION — round()
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains Python's built-in round() function:

#       - what round() does
#       - how round() works with integers and floats
#       - how round() handles negative numbers
#       - how round() handles ties (round half to even)
#       - when to use round() vs other rounding functions
#
# ============================================================

print("\n# -----------------------------")
print("# 1. WHAT round() DOES")
print("# -----------------------------\n")

# round() rounds a number to a given number of decimal places (default is 0).
# It returns an integer if no decimal places are specified, otherwise it returns a float.
print(round(3.14159))  # 3
print(round(2.71828, 2))  # 2.72
print(round(-1.5))  # -2
print(round(2.5))   # 2 (round half to even)
print(round(3.5))   # 4 (round half to even)    