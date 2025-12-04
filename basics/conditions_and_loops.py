# ============================================================
#            LESSON — CONDITIONS & LOOPS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# 
# Description:
#  This lesson covers conditions and loops in Python:   
#  if, elif, else statements, for loops, while loops,
#  break and continue statements, nested loops, and
#  practical input validation examples.
#
# Contents:
#   1. Conditions — if / elif / else
#   2. For loops
#   3. While loops
#   4. break and continue
#   5. Nested loops
#   6. Input validation examples
#
# ==============================================

# --------------------------------------------------------------
# 1. CONDITIONS — if / elif / else
# --------------------------------------------------------------

x = 15

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")

# Comparison operators:
# >, <, >=, <=, ==, !=

# Logical operators:
# and, or, not

age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")

# --------------------------------------------------------------
# 2. FOR LOOPS
# --------------------------------------------------------------

print("\nFOR loop from 1 to 5:")
for i in range(1, 6):
    print(i)

# Looping through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# --------------------------------------------------------------
# 3. WHILE LOOPS
# --------------------------------------------------------------

print("\nWhile loop countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Lift off!")

# --------------------------------------------------------------
# 4. BREAK and CONTINUE
# --------------------------------------------------------------

print("\nBREAK example:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\nCONTINUE example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # prints only odd numbers

# --------------------------------------------------------------
# 5. NESTED LOOPS
# --------------------------------------------------------------

print("\nMultiplication table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

# --------------------------------------------------------------
# 6. INPUT VALIDATION EXAMPLES
# --------------------------------------------------------------

print("\nAsk user for a valid number:")

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        number = int(user_input)
        print(f"Thank you! You entered {number}")
        break
    else:
        print("Invalid input, try again.")
