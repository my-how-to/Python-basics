# ============================================================
#            LESSON — BITWISE XOR (^)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Focused introduction to the XOR operator:
#   toggling bits and finding differences.
#
# Contents:
#   1. Quick intuition
#   2. XOR basics
#   3. Typical use cases
#   4. Mini example
#
# ============================================================

print("\n# -----------------------------")
print("# 1. QUICK INTUITION")
print("# -----------------------------\n")

# XOR keeps a bit if the sides differ.
# 1 ^ 1 -> 0
# 1 ^ 0 -> 1
# 0 ^ 1 -> 1
# 0 ^ 0 -> 0


print("\n# -----------------------------")
print("# 2. XOR BASICS")
print("# -----------------------------\n")

start = 0b1000  # 8
toggle = 0b0010 # 2
flipped = start ^ toggle
print("start:   ", format(start, "04b"))
print("toggle:  ", format(toggle, "04b"))
print("XOR:     ", format(flipped, "04b"), "->", flipped)
# 1000
# 0010
# ----
# 1010 -> 10


print("\n# -----------------------------")
print("# 3. TYPICAL USE CASES")
print("# -----------------------------\n")

# Common use cases for XOR:
#   1) Toggling specific bits in a bitmask.
#   2) Simple encryption/decryption by XORing with a key.
#   3) Swapping two values without a temporary variable.
#   4) Finding a unique element when all others appear twice.

# XOR with the same mask twice returns to original.
back = flipped ^ toggle
print("XOR twice ->", format(back, "04b"), "(same as start)")


print("\n# -----------------------------")
print("# 4. MINI EXAMPLE")
print("# -----------------------------\n")

# 1 Toggling specific bits in a bitmask with XOR.
# Example: toggling the 2nd bit of a byte. Usually done with OR, but XOR can toggle.
# this is useful for feature flags or settings.
bitmask = 0b0001  # initial bitmask
toggle_mask = 0b0010  # mask to toggle 2nd bit
new_bitmask = bitmask ^ toggle_mask
print("bitmask:     ", format(bitmask, "04b"))      # 0001
print("toggle_mask: ", format(toggle_mask, "04b"))  # 0010
print("new_bitmask: ", format(new_bitmask, "04b"))  # 0011


# 2 Simple encryption/decryption by XORing with a key.
key = 0b1111  # example key
original = 0b1010  # 10
encrypted = original ^ key
decrypted = encrypted ^ key
print("original:  ", format(original, "04b"))
print("encrypted: ", format(encrypted, "04b"))
print("decrypted: ", format(decrypted, "04b"), "(same as original)")


# 3 Swapping two values without a temporary variable.
a = 1           # 1 (01) in binary
b = 0           # 0 (00) in binary
a = a ^ b       # a now 1 (01)  b is 0
b = a ^ b       # b now 1 (01)  a is 1 (01)
# here a is 1 (01) and b is 1 (01)
# now swap back
a = a ^ b # a now 0 (00) b is 1 (01)
# now a is 0 and b is 1


# 4 Find the unique element in a list where every other element appears twice.
data = [4, 1, 2, 1, 2]
unique = 0
for num in data:
    unique ^= num
print("Unique element in", data, "is", unique)
