# ==========================================================
#                       int()
# ==========================================================
#
# 1) WHAT IS int()?
#
# int() converts a value into an integer.
#
# It can convert:
# - strings
# - floats
# - booleans
# - numbers in different bases (binary, octal, hex)
#
# Return value:
# - integer (int)
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# int(x)
# int(x, base)
#
# x     → value to convert
# base  → numeric base (only used when x is a string)
#
# Default base = 10
#
# ==========================================================
# 3) BASIC CONVERSIONS
# ==========================================================

# ---------- STRING TO INT ----------

print(int("10"))
# Output: 10


# ---------- FLOAT TO INT ----------
# NOTE: It truncates (does NOT round)

print(int(3.9))
# Output: 3


# ---------- BOOLEAN TO INT ----------

print(int(True))   # 1
print(int(False))  # 0


# ==========================================================
# 4) USING BASE (NUMBER SYSTEMS)
# ==========================================================
#
# int(string, base)
#
# Common bases:
# 2   → binary
# 8   → octal
# 10  → decimal
# 16  → hexadecimal

# ---------- BINARY ----------

print(int("1010", 2))
# Output: 10


# ---------- OCTAL ----------

print(int("12", 8))
# Output: 10


# ---------- HEXADECIMAL ----------

print(int("A", 16))
# Output: 10


# ==========================================================
# 5) IMPORTANT RULES
# ==========================================================
#
# ✔ When using base:
#   - Input MUST be string
#
# ✔ Valid digits depend on base:
#   - Base 2 → only 0 and 1
#   - Base 8 → 0–7
#   - Base 16 → 0–9 and A–F
#
# ✔ Spaces are allowed:
#   int("   42   ") → 42
#
# ==========================================================
# 6) COMMON ERRORS
# ==========================================================

# ❌ Invalid literal
# int("abc")
# ValueError

# ❌ Wrong digit for base
# int("2", 2)
# ValueError

# ❌ Base with non-string
# int(10, 2)
# TypeError


# ==========================================================
# 7) TRUNCATION BEHAVIOR
# ==========================================================
#
# int() removes decimal part (does NOT round)

print(int(-3.9))
# Output: -3   (toward zero)


# ==========================================================
# 8) HOW IT WORKS CONCEPTUALLY
# ==========================================================
#
# For numbers:
#   → removes fractional part
#
# For strings:
#   → parses digits according to base
#
# Time complexity:
#   O(n) for string conversion
#
# ==========================================================
# 9) int() vs round()
# ==========================================================
#
# int(3.9)     → 3
# round(3.9)   → 4
#
# int() truncates.
# round() rounds.
#
# ==========================================================
# 10) KEY RULES
# ==========================================================
#
# - Converts value to integer.
# - Can parse different bases.
# - Truncates floats.
# - Raises ValueError on invalid strings.
# - Returns int type.
#
# ==========================================================
# END OF LESSON
# ==========================================================