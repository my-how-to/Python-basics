# ============================================================
#            LESSON — NUMERIC LITERALS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Explains Python’s literal notation for integers and floats:
#   decimal, binary, octal, hexadecimal, underscores for readability,
#   floating-point forms, and scientific notation.
#
# A literal is a direct value written in code — the interpreter reads
# it as-is without needing a variable or calculation to produce it.
#
# Contents:
#   1. Decimal integers (default)
#   2. Binary literals (0b / 0B)
#   3. Octal literals (0o / 0O)
#   4. Hexadecimal literals (0x / 0X)
#   5. Readable numbers with underscores
#   6. Floating-point literals
#   7. Scientific notation (exponent form)
#
# ============================================================


print("\n# -----------------------------")
print("# 1. DECIMAL INTEGERS (DEFAULT)")
print("# -----------------------------\n")

# Everyday math: budgets, counters, measurements, and general arithmetic.
budget = 4500        # same as 4_500
temperature = -12
print("Budget:", budget)
print("Temperature:", temperature)


print("\n# -----------------------------")
print("# 2. BINARY LITERALS")
print("# -----------------------------\n")

# Common in bit masks, permissions, embedded systems, and low-level protocols.
permission_flags = 0b1010  # binary for decimal 10
print("permission_flags (binary):", bin(permission_flags))
print("As decimal:", permission_flags)


print("\n# -----------------------------")
print("# 3. OCTAL LITERALS")
print("# -----------------------------\n")

# Mostly used when dealing with UNIX file permissions or legacy data formats.
file_mode = 0o755  # common UNIX permission mask
print("file_mode (octal):", oct(file_mode))
print("As decimal:", file_mode)


print("\n# -----------------------------")
print("# 4. HEXADECIMAL LITERALS")
print("# -----------------------------\n")

# Handy for color codes, memory addresses, checksums, and debugging bytes.
rgb_color = 0xFF8800
print("rgb_color (hex):", hex(rgb_color))
print("As decimal:", rgb_color)


print("\n# -----------------------------")
print("# 5. READABLE NUMBERS WITH UNDERSCORES")
print("# -----------------------------\n")

# Use underscores in large values to reduce mistakes when reading or editing.
population = 7_888_000_000
credit_card_mask = 0xFFFF_FFFF_FFFF_FFFF
print("Population:", population)
print("Credit card mask:", hex(credit_card_mask))

# Underscores are ignored by Python; they are purely for humans.


print("\n# -----------------------------")
print("# 6. FLOATING-POINT LITERALS")
print("# -----------------------------\n")

# Measurements, percentages, currency with cents, and any fractional quantities.
pi_approx = 3.14159
high_precision = 0.000250
trailing = 5.0  # still a float
print("pi:", pi_approx)
print("small value:", high_precision)
print("trailing decimal:", trailing)

print(0.1 + 0.2 == 0.3)
# In Python, the expression 0.1 + 0.2 == 0.3 evaluates to False because 
# floating-point numbers are stored using IEEE 754 binary representation, 
# and many decimal fractions (including 0.1, 0.2, and 0.3) cannot be represented exactly in binary. 
# As a result, 0.1 + 0.2 produces a value slightly different from the mathematical 
# 0.3 (approximately 0.30000000000000004), so an exact equality comparison fails. 
# The order of + and == does not change the outcome here because operator precedence 
# ensures that addition is evaluated before comparison (+ has higher precedence than ==), 
# meaning the sum is computed first and then compared. 
# 
# In general, you should never compare floating-point numbers using == due to precision artifacts; 
# instead, compare within a tolerance, for example abs(a - b) < 1e-9, 
abs((0.1 + 0.2) - 0.3) < 1e-9

# or preferably use math.isclose(a, b) from the standard library, 
# which is designed specifically for safe floating-point comparisons.
import math
math.isclose(0.1 + 0.2, 0.3)

print("\n# -----------------------------")
print("# 7. SCIENTIFIC NOTATION")
print("# -----------------------------\n")

# Express very large/small values elegantly: physics constants, tolerances, etc.
avogadro = 6.022e23     # 6.022 × 10^23
microscopic = 4.2e-7    # 4.2 × 10^-7
print("Avogadro's number:", avogadro)
print("Microscopic value:", microscopic)
