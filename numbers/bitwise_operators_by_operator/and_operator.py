# ============================================================
#            LESSON — BITWISE AND (&)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Focused introduction to the AND operator:
#   masking bits and testing flags.
#
# Contents:
#   1. Quick intuition
#   2. AND basics
#   3. Typical use cases
#   4. Mini example
#
# ============================================================

print("\n# -----------------------------")
print("# 1. QUICK INTUITION")
print("# -----------------------------\n")

# AND keeps a bit only if both sides have 1.
# 1 & 1 -> 1
# 1 & 0 -> 0
# 0 & 1 -> 0
# 0 & 0 -> 0


print("\n# -----------------------------")
print("# 2. AND BASICS")
print("# -----------------------------\n")

number = 0b1101  # 13
mask = 0b0101    # 5
result = number & mask
print("number:", format(number, "04b"))
print("mask:  ", format(mask, "04b"))
print("AND:   ", format(result, "04b"), "->", result)
# 1101
# 0101
# ----
# 0101 -> 5


print("\n# -----------------------------")
print("# 3. TYPICAL USE CASES")
print("# -----------------------------\n")

# Common use cases for AND:
#   1) Masking: keep only selected bits.
#   2) Testing: check if a bit is set.
#   3) Clearing: turn off specific bits with AND + NOT.

# Test if a bit is set (4's place).
bit_to_test = 0b0100
is_set = (number & bit_to_test) != 0
print("3rd bit set?", is_set)


print("\n# -----------------------------")
print("# 4. MINI EXAMPLE")
print("# -----------------------------\n")

# Extract the low 4 bits of a number.
value = 0b1011_1101
low_nibble = value & 0b1111
print("value:", format(value, "08b"))
print("low 4 bits:", format(low_nibble, "04b"), "->", low_nibble)
