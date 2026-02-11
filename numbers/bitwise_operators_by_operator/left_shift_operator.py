# ============================================================
#            LESSON — BITWISE LEFT SHIFT (<<)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Focused introduction to left shift:
#   moving bits left and multiplying by powers of two.
#
# Contents:
#   1. Quick intuition
#   2. Left shift basics
#   3. Typical use cases
#   4. Mini example
#
# ============================================================

print("\n# -----------------------------")
print("# 1. QUICK INTUITION")
print("# -----------------------------\n")

# Shifting left by n is like multiplying by 2^n. 
# It is like 3 * 2 ** n.

# 0    << 1 -> 0000 (0 becomes 0)
# 01   << 1 -> 0010 (1 becomes 2)
# 0011 << 1 -> 0110 (3 becomes 6)
# 0011 << 2 -> 1100 (3 becomes 12)


print("\n# -----------------------------")
print("# 2. LEFT SHIFT BASICS")
print("# -----------------------------\n")

base = 3
print("base:", base, "binary:", format(base, "04b"))
print("base << 1:", base << 1, "binary:", format(base << 1, "04b")) # 6
print("base << 2:", base << 2, "binary:", format(base << 2, "04b")) # 12


print("\n# -----------------------------")
print("# 3. TYPICAL USE CASES")
print("# -----------------------------\n")

# Common use cases for left shift:
#   1) Building bit masks (1 << position).
#   2) Fast multiplication by powers of two.
#   3) Packing values into bit fields.

# Build a mask for bit 5.
mask = 1 << 5
print("bit 5 mask:", format(mask, "08b"), "->", mask)


print("\n# -----------------------------")
print("# 4. MINI EXAMPLE")
print("# -----------------------------\n")

# Pack two 4-bit values into one byte.
low = 0b1010
high = 0b0101
packed = (high << 4) | low
print("packed:", format(packed, "08b"), "->", packed) # 01011010 -> 90

print("\n# -----------------------------")
print("# 5. with other operators")
print("# -----------------------------\n")

