# ==========================================================
#           BITWISE OPERATORS & ORDER OF PRECEDENCE
# ==========================================================
#
# 1) WHAT ARE BITWISE OPERATORS?
#
# Bitwise operators work at the binary (bit) level.
# They operate on integers.
#
# Example:
# 5  ->  0101
# 3  ->  0011
#
# Bitwise operations manipulate these bits directly.
#
# ==========================================================
# 2) LIST OF BITWISE OPERATORS
# ==========================================================
#
# &   → AND
# |   → OR
# ^   → XOR
# ~   → NOT (bitwise inversion)
# <<  → Left Shift
# >>  → Right Shift
#
# ==========================================================
# 3) WHAT EACH OPERATOR DOES
# ==========================================================
#
# &  (AND)
# 1 if BOTH bits are 1
#
# 5 & 3
# 0101
# 0011
# ----
# 0001  → 1
#
# |  (OR)
# 1 if at least one bit is 1
#
# 5 | 3  → 7
#
# ^  (XOR)
# 1 if bits are DIFFERENT
#
# 5 ^ 3  → 6
#
# ~  (NOT)
# Inverts bits
#
# ~5
# 5  = 00000101
# ~5 = 11111010  (two's complement representation)
# Result: -6
#
# << (Left Shift)
# Shifts bits left (multiply by 2^n)
#
# 5 << 1  → 10
#
# >> (Right Shift)
# Shifts bits right (divide by 2^n)
#
# 5 >> 1  → 2
#
# ==========================================================
# 4) ORDER OF PRECEDENCE (HIGH → LOW)
# ==========================================================
#
# 1. ~        (bitwise NOT)
# 2. <<, >>   (shifts)
# 3. &        (AND)
# 4. ^        (XOR)
# 5. |        (OR)
#
# Important:
# Bitwise operators have LOWER precedence than arithmetic
# operators (+, -, *, /).
#
# Example:
#
# 5 + 3 & 1
#
# Step 1: 5 + 3 = 8
# Step 2: 8 & 1 = 0
#
# Because + runs before &
#
# ==========================================================
# 5) EXAMPLE OF PRECEDENCE
# ==========================================================
#
# expression:
#
# 5 | 3 & 1
#
# Step 1: 3 & 1 = 1
# Step 2: 5 | 1 = 5
#
# Because & has higher precedence than |
#
# ==========================================================
# 6) RECOMMENDED PRACTICE
# ==========================================================
#
# Always use parentheses for clarity:
#
# result = (5 | 3) & 1
#
# Makes evaluation explicit and avoids mistakes.
#
# ==========================================================
# 7) TIME COMPLEXITY
# ==========================================================
#
# All bitwise operations are O(1)
# They operate directly at CPU level.
#
# ==========================================================
# 8) KEY RULES
# ==========================================================
#
# - Work only on integers.
# - Operate on binary representation.
# - Precedence matters.
# - Use parentheses for clarity.
# - Frequently tested in certification exams.
#
# ==========================================================
# END OF LESSON
# ==========================================================