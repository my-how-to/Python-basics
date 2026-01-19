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

for i in range(20):
    for j in range(10):
        print(i, j, " or ", i | j, end=" | ")
        print()

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
feature_flag = 0b1000 # 8
flags |= feature_flag
print("flags after set:", format(flags, "04b")) # 1010 (10) as bit 3 is set.


print("\n# -----------------------------")
print("# 4. MINI EXAMPLE")
print("# -----------------------------\n")

# Build a mask from a list of bit positions.
positions = [0, 2, 4]  # set bits 0, 2, 4
mask = 0
for p in positions:
    mask |= (1 << p)
print("mask from positions:", format(mask, "08b"), "->", mask)

# 2) Combining: merge multiple flags.
combined_flags = 0b0001  # initial flags
new_flags = [0b0010, 0b0100, 0b100] # flags to add
for nf in new_flags:
    combined_flags |= nf
print("combined flags:", format(combined_flags, "04b"), "->", combined_flags)   
# Result is 1111 (15) as all flags are combined.

# 3) Defaults: add capabilities without removing others.
default_caps = 0b0101  # default capabilities
additional_caps = 0b1010  # additional capabilities
all_caps = default_caps | additional_caps
print("all capabilities:", format(all_caps, "04b"), "->", all_caps)
# Result is 1111 (15) as all capabilities are included.