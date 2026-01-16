# ============================================================
#            LESSON — BITWISE OR (|)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Focused introduction to the OR operator:
#   setting bits and combining flags.
#
# Contents:
#   1. Quick intuition
#   2. OR basics
#   3. Typical use cases
#   4. Mini example
#
# ============================================================

print("\n# -----------------------------")
print("# 1. QUICK INTUITION")
print("# -----------------------------\n")

# OR keeps a bit if either side has 1.
# 1 | 1 -> 1
# 1 | 0 -> 1
# 0 | 1 -> 1
# 0 | 0 -> 0


print("\n# -----------------------------")
print("# 2. OR BASICS")
print("# -----------------------------\n")

flags = 0b0010  # 2
enable = 0b1000 # 8
combined = flags | enable
print("flags:   ", format(flags, "04b"))
print("enable:  ", format(enable, "04b"))
print("OR:      ", format(combined, "04b"), "->", combined)
# 0010
# 1000
# ----
# 1010 -> 10


print("\n# -----------------------------")
print("# 3. TYPICAL USE CASES")
print("# -----------------------------\n")

# Common use cases for OR:
#   1) Setting: turn on a bit in a mask.
#   2) Combining: merge multiple flags.
#   3) Defaults: add capabilities without removing others.

# Set a feature flag (8's place).
feature_flag = 0b1000
flags |= feature_flag
print("flags after set:", format(flags, "04b"))


print("\n# -----------------------------")
print("# 4. MINI EXAMPLE")
print("# -----------------------------\n")

# Build a mask from a list of bit positions.
positions = [0, 2, 4]  # set bits 0, 2, 4
mask = 0
for p in positions:
    mask |= (1 << p)
print("mask from positions:", format(mask, "08b"), "->", mask)
