# ============================================================
#            LESSON — BITWISE NOT (~)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Focused introduction to the NOT operator:
#   inverting bits and understanding two's complement.
#
# Contents:
#   1. Quick intuition
#   2. NOT basics
#   3. Typical use cases
#   4. Mini example
#
# ============================================================

print("\n# -----------------------------")
print("# 1. QUICK INTUITION")
print("# -----------------------------\n")

# NOT flips every bit.
# In Python, ~x equals -(x + 1) because integers are unbounded.


print("\n# -----------------------------")
print("# 2. NOT BASICS")
print("# -----------------------------\n")

num = 6
print("num:", num, "binary:", format(num, "08b"))
print("~num:", ~num, "(equals -(num + 1))") # -(6 + 1) = -7

for i in range(10):
    print(~i, end=" ")  # prints -1, -2, -3, ..., -10



print("\n# -----------------------------")
print("# 3. TYPICAL USE CASES")
print("# -----------------------------\n")

# Common use cases for NOT:
#   1) Clearing bits with AND + NOT.
#   2) Creating inverse masks in a fixed width.
#   3) Bitwise complement in protocols or encodings.

# Clear a bit using AND + NOT.
# This is often used to turn off specific bits in a bitmask.
# a bitmask is a sequence of bits that can enable or disable certain features.
flags = 0b1111
bit_to_clear = 0b0010
flags &= ~bit_to_clear # clear the 2nd bit
print("flags after clear:", format(flags, "04b")) # 1101


print("\n# -----------------------------")
print("# 4. MINI EXAMPLE")
print("# -----------------------------\n")

# Show a fixed-width inversion using a mask.
width_mask = 0b1111  # 4-bit mask
fixed_invert = (~num) & width_mask
print("4-bit inverted:", format(fixed_invert, "04b"), "->", fixed_invert)
