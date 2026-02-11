# ============================================================
#            LESSON — OPERATORS & EXPRESSIONS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson introduces operators and expressions in Python:
#   what expressions are, arithmetic operators, comparison
#   operators, logical operators, assignment operators, operator
#   precedence, and practical mini-examples.    
#
# Contents:
#   1. What is an expression?
#   2. Arithmetic operators
#   3. Exponent operator (**)
#   4. Comparison operators
#   5. Logical operators
#   6. Assignment operators
#   7. Operator precedence
#   8. Practical mini-examples
#
# ============================================================


print("\n# -----------------------------")
print("# 1. WHAT IS AN EXPRESSION?")
print("# -----------------------------\n")

# An expression is a combination of values and operators.
# Python evaluates it and produces a result.

result = 5 + 3 * 2
print("Result of 5 + 3 * 2 =", result)

# Output:
# 11


print("\n# -----------------------------")
print("# 2. ARITHMETIC OPERATORS")
print("# -----------------------------\n")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)            # '/' always yields a float (2 / 1 -> 2.0); use '//' or int() to get integers.
print("Floor Division:", a // b)     # removes decimal. Discards the fractional part and returns an integer (or float if operands are float).
print("Modulus:", a % b)             # remainder
print("Exponent:", a ** b)           # power

# Modulus example explanation:
# 10 // 3 = 3   (3 * 3 = 9)
# 10 - 9 = 1    (remainder)

print("\n# -----------------------------")
print("# 3. EXPONENT OPERATOR (**)")
print("# -----------------------------\n")

# Exponentiation raises a number to a power: base ** exponent.
print("2 ** 3 =", 2 ** 3)     # 8
print("5 ** 0 =", 5 ** 0)     # 1
print("2 ** -3 =", 2 ** -3)   # 0.125 (reciprocal)
print("9 ** 0.5 =", 9 ** 0.5) # 3.0 (square root) 3 to the power of 2 is 9
print("27 ** (1/3) =", 27 ** (1/3)) # 3.0 (cube root) 3 to the power of 3 is 27
print("16 ** 0.25 =", 16 ** 0.25) # 2.0 (fourth root) 2 to the power of 4 is 16

# Exponentiation is right-associative:
# 2 ** 3 ** 2 is 2 ** (3 ** 2) = 2 ** 9 = 512.
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)

# Parentheses make intent explicit.
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)  # 64

print("\n# -----------------------------")
print("# 4. COMPARISON OPERATORS")
print("# -----------------------------\n")

x = 5
y = 7

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# Example Output:
# x == y: False
# x != y: True
# x > y: False
# x < y: True
# x >= y: False
# x <= y: True


print("\n# -----------------------------")
print("# 5. LOGICAL OPERATORS")
print("# -----------------------------\n")

# Logical Operators (and, or) DO NOT Return Booleans
print(5 and 0)      # 0, because 0 is falsy
print(0 or 7)       # 7
print("" and "Hi")  # ""
print("Hello" or "")# "Hello"

is_admin = True
is_active = False

print("AND:", is_admin and is_active) # False
print("OR:", is_admin or is_active) # True
print("NOT:", not is_admin)

# Example Output:
# AND: False
# OR: True
# NOT: False

# Identity check: "is" checks if two variables point to the same object.
value = None
print("Is None?", value is None) # True, because value is exactly None (the singleton object representing "no value")
print("Is not None?", value is not None) # False, because value is None, so it is not "not None"
print("5 is 5.0:", 5 is 5.0) # False, different types
print("5 == 5.0:", 5 == 5.0) # True, same value


print("\n# -----------------------------")
print("# 6. ASSIGNMENT OPERATORS")
print("# -----------------------------\n")

value = 10
print("Start:", value)

value += 5  # value = value + 5
print("After += 5:", value)

value -= 3
print("After -= 3:", value)

value *= 2
print("After *= 2:", value)

value //= 4 # value = value // 4
print("After //= 4:", value)

# Example Output:
# Start: 10
# After += 5: 15
# After -= 3: 12
# After *= 2: 24
# After //= 4: 6

# order of operations matters:
x = 3
x += x == 3
print(x) # Output: 4 (x == 3 is True, which is 1 when added to x)
# This is a common pattern where the result of a comparison (True/False) is used in an arithmetic operation. 
# In this case, since x == 3 is True, it evaluates to 1, and x becomes 3 + 1 = 4.

print("\n# -----------------------------")
print("# 7. OPERATOR PRECEDENCE")
print("# -----------------------------\n")

# Python evaluates according to rules (PEMDAS):
# Parentheses, Exponent, Multiplication/Division, Addition/Subtraction.

expr1 = 2 + 3 * 4
expr2 = (2 + 3) * 4

print("Without parentheses:", expr1)    # Without parentheses: 14
print("With parentheses:", expr2)       # With parentheses: 20

# Exponentiation (`**`) is also special: it is evaluated right-to-left.
# Example: 2 ** 3 ** 2 is 2 ** (3 ** 2) = 512.
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)  # Output: 512

# Modulus and floor division have the same precedence as multiplication/division.
print(10 % 3 * 2) # Output: 2, because it's evaluated as (10 % 3) * 2 = 1 * 2 = 2

# bitwise operators have lower precedence than arithmetic operators, but higher than comparison operators.
result = 1 << 2 + 1
print("1 << 2 + 1 =", result) # Output: 8, because it's evaluated as 1 << (2 + 1) = 1 << 3 = 8


print("\n# -----------------------------")
print("# 8. PRACTICAL MINI-EXAMPLES")
print("# -----------------------------\n")

print("# Example 1 — Checking age range")
age = 17
print("Is teenager?", age >= 13 and age <= 19)

print("\n# Example 2 — Password check")
password = "secret123"
print("Password too short?", len(password) < 8)

print("\n# Example 3 — Calculating discount")
price = 100
discount_rate = 0.2
final_price = price - price * discount_rate
print("Final price:", final_price)

# Example Output:
# Is teenager? True
# Password too short? False
# Final price: 80.0


# Extra Example — Using modulus operator
x = 11
y = 4

x = x % y # x now holds the remainder of 11 divided by 4
print (x, y)    # Output: 3 4

x = x % y # reapplying % with unchanged values gives the same result
print (x, y)    # Output: 3 4

y = y % x # y now holds the remainder of 4 divided by 3
print (y)       # Output: 1


print("\nVisualizing i % 4 values:")

for i in range(20):
    print(f"i: {i}, i % 4: {i % 4}")


print("\nVisualizing i // 4 values:")

for i in range(20):
    print(f"i: {i}, i // 4: {i // 4}")



