# ============================================================
#            LESSON — BITWISE OPERATORS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   A practical introduction to bitwise operators in Python:
#   AND, OR, XOR, NOT, shifts, masks, and common patterns.
#
# Contents:
#   1. Bits and binary display
#   2. AND (&): masking bits
#   3. OR (|): setting bits
#   4. XOR (^): toggling bits
#   5. NOT (~): bitwise inversion
#   6. Shifts (<<, >>): move bits
#   7. Bit flags: set, clear, toggle, test
#   8. Practical mini-exercises
#
# ============================================================

print("\n# -----------------------------")
print("# 1. BITS AND BINARY DISPLAY")
print("# -----------------------------\n")

# Integers are stored in binary. bin() shows their bits.
# a bit is a 0 or 1 representing off/on.
value = 13  # 1101 in binary
print("value:", value)
print("binary:", bin(value)) # 0b1101

# Padding with zeros helps visualize widths. 
# 08b means 8 bits, padded with leading zeros.
print("8-bit view:", format(value, "08b")) # 00001101

# -----------------------------
# 1.1 QUICK MENTAL SHORTCUTS
# -----------------------------
# Handy reminders when doing bitwise operations in your head.

# &  -> keeps overlapping 1-bits
# |  -> keeps any 1-bits
# ^  -> keeps bits that differ
# << n -> multiply by 2^n
# >> n -> integer-divide by 2^n
# ~x -> equals -(x + 1) in Python


print("\n# -----------------------------")
print("# 2. AND (&): MASKING BITS")
print("# -----------------------------\n")

# AND keeps a bit only if both sides have 1.
number = 0b1101  # 13
mask = 0b0101    # 5
result = number & mask
print("number:", format(number, "04b")) # 04b means 4 bits, padded with leading zeros
print("mask:  ", format(mask, "04b"))
print("AND:   ", format(result, "04b"), "->", result) # 0101 -> 5
# 1101
# 0101
# ----
# 0101

# Typical use: check if a bit is set.
# Is the 3rd bit (4's place) set?
bit_to_test = 0b0100
is_set = (number & bit_to_test) != 0
print("3rd bit set?", is_set) # True because 1101 & 0100 = 0100 != 0


print("\n# -----------------------------")
print("# 3. OR (|): SETTING BITS")
print("# -----------------------------\n")

# OR sets a bit if either side has 1.
flags = 0b0010  # 2
enable = 0b1000 # 8
combined = flags | enable
print("flags:   ", format(flags, "04b"))
print("enable:  ", format(enable, "04b"))
print("OR:      ", format(combined, "04b"), "->", combined) # 1010 -> 10
# 0010
# 1000
# ----
# 1010

# Typical use: add a permission or feature flag.


print("\n# -----------------------------")
print("# 4. XOR (^): TOGGLING BITS")
print("# -----------------------------\n")

# why use XOR?
# XOR is useful for toggling bits, swapping values without a temporary variable, and checking differences.

# list of common use cases for XOR:
#   1) Toggling specific bits in a bitmask.
#   2) Simple encryption/decryption by XORing with a key.
#   3) Swapping two variables without a temporary variable.
#   4) Finding the unique element in a list where every other element appears twice.

# XOR flips a bit if exactly one side has 1. otherwise, it becomes 0.
start = 0b1000 # 8
toggle = 0b0010 # 2
flipped = start ^ toggle
print("start:   ", format(start, "04b"))
print("toggle:  ", format(toggle, "04b"))
print("XOR:     ", format(flipped, "04b"), "->", flipped) # 1010 -> 10
# 1000
# 0010
# ----
# 1010 -> 10

# a list with every element twice except one
data = [4, 1, 2, 1, 2]
unique = 0
for num in data:
    unique ^= num
print("Unique element in", data, "is", unique)  # 4




# XOR with the same mask twice returns to original.
back = flipped ^ toggle
print("XOR twice ->", format(back, "04b"), "(same as start)")

a = 1           # 1 (01) in binary
b = 0           # 0 (00) in binary
a = a ^ b       # a now 1 (01)  b is 0 (00) unchanged
b = a ^ b       # b now 1 (01)  a is 1 (01) unchanged
# here a is 1 (01) and b is 1 (01)
# now swap back
a = a ^ b # a now 0 (00) b is 1 (01) unchanged
print("Swapped a,b:", a, b)  # Expected: 0 1

print("\n# -----------------------------")
print("# 5. NOT (~): BITWISE INVERSION")
print("# -----------------------------\n")

# ~ flips every bit, but Python integers are unbounded.
# So ~x equals -(x + 1) due to two's complement rules.
num = 6
print("num:", num, "binary:", format(num, "08b"))
print("~num:", ~num, "(equals -(num + 1))") # -7

# To see a fixed-width inversion, mask it down.
width_mask = 0b1111  # 4-bit mask
fixed_invert = (~num) & width_mask
print("4-bit inverted:", format(fixed_invert, "04b"), "->", fixed_invert)


print("\n# -----------------------------")
print("# 6. SHIFTS (<<, >>): MOVE BITS")
print("# -----------------------------\n")

# Left shift multiplies by powers of two.
base = 3
print("base:", base, "binary:", format(base, "04b"))
print("base << 1:", base << 1, "binary:", format(base << 1, "04b"))
print("base << 2:", base << 2, "binary:", format(base << 2, "04b"))

# Right shift divides by powers of two (floor for positives).
value = 20
print("value:", value, "binary:", format(value, "08b"))
print("value >> 1:", value >> 1)
print("value >> 2:", value >> 2)


print("\n# -----------------------------")
print("# 7. BIT FLAGS: SET, CLEAR, TOGGLE, TEST")
print("# -----------------------------\n")

# Define flag bits.
READ = 0b0001
WRITE = 0b0010
EXEC = 0b0100

permissions = 0b0000

# Set bits with OR.
permissions |= READ
permissions |= EXEC
print("set READ + EXEC:", format(permissions, "04b"))

# Test bits with AND.
can_write = (permissions & WRITE) != 0
print("can_write?", can_write)

# Toggle with XOR.
permissions ^= EXEC
print("toggle EXEC:", format(permissions, "04b"))

# Clear bits with AND + NOT.
permissions &= ~READ
print("clear READ:", format(permissions & 0b1111, "04b"))


print("\n# -----------------------------")
print("# 8. PRACTICAL MINI-EXERCISES")
print("# -----------------------------\n")

# Exercise 1: Extract the low 4 bits of a number.
value = 0b1011_1101
low_nibble = value & 0b1111
print("value:", format(value, "08b"))
print("low 4 bits:", format(low_nibble, "04b"), "->", low_nibble)

# Exercise 2: Check if a number is odd using a bit test.
for n in range(6):
    is_odd = (n & 1) == 1
    print(f"{n} odd?", is_odd)

# Exercise 3: Build a simple mask from a list of bit positions.
positions = [0, 2, 4]  # set bits 0, 2, 4
mask = 0
for p in positions:
    mask |= (1 << p)
print("mask from positions:", format(mask, "08b"), "->", mask)


print("\n# -----------------------------")
print("# 9. QUICK EXAMPLE + SOLUTION")
print("# -----------------------------\n")

# Example: compute each result mentally, then check.
x = 3       # 0011 in binary
y = 1       # 0001 in binary

a = x & y   # AND of x and y.                       | Rule: 1 only if both bits are 1.
b = x | y   # OR of x and y .                       | Rule: 1 if either bit is 1.
c = ~x      # Inversion of x (in Python, equals -(x + 1)) 
d = x ^ 4   # XOR of x with 4 (0100 in binary)      | Rule: 1 if bits are different.
e = x >> 2  # Right shift x by 2                    | Rule: divide by 4 (2^2).
f = x << 2  # Left shift x by 2                     | Rule: multiply by 4 (2^2).
print(a, b, c, d, e, f)  # Expected: 1 3 -4 7 0 12
