# ============================================================
#            LESSON — BITWISE RIGHT SHIFT (>>)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Focused introduction to right shift:
#   moving bits right and dividing by powers of two.
#
# Contents:
#   1. Quick intuition
#   2. Right shift basics
#   3. Typical use cases
#   4. Mini example
#
# ============================================================

print("\n# -----------------------------")
print("# 1. QUICK INTUITION")
print("# -----------------------------\n")

# Shifting right by n is like integer division by 2^n (for positives). 
# it is like 12 // 2 ** n 
# 1100 >> 1 -> 0110 (12 becomes 6)
# 1100 >> 2 -> 0011 (12 becomes 3)


print("\n# -----------------------------")
print("# 2. RIGHT SHIFT BASICS")
print("# -----------------------------\n")

value = 20
print("value:", value, "binary:", format(value, "08b"))
print("value >> 1:", value >> 1) # 10
print("value >> 2:", value >> 2) # 5


print("\n# -----------------------------")
print("# 3. TYPICAL USE CASES")
print("# -----------------------------\n")

# Common use cases for right shift:
#   1) Fast division by powers of two.
#   2) Extracting high-order bits.
#   3) Walking through packed fields.

# Extract the high 4 bits of a byte.
byte = 0b1011_1101
high_nibble = byte >> 4
print("byte:", format(byte, "08b"))
print("high 4 bits:", format(high_nibble, "04b"), "->", high_nibble)


print("\n# -----------------------------")
print("# 4. MINI EXAMPLE")
print("# -----------------------------\n")

# Unpack two 4-bit values from one byte.
packed = 0b0101_1010
high = packed >> 4
low = packed & 0b1111
print("high:", format(high, "04b"), "->", high)
print("low: ", format(low, "04b"), "->", low)
