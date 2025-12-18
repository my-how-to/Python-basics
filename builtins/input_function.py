# ============================================================
#                 BUILT-IN FUNCTION — input()
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   A guided tour of Python's input() for interactive scripts:
#       1. How it pauses execution and always returns a string
#       2. Prompt messages and newline handling
#       3. Converting string responses to numbers
#       4. Splitting multiple values from one line
#       5. Guarding against invalid entries with try/except
#       6. Mini practice exercises
#
# Run this file and answer the prompts in your terminal.
# ============================================================

import math

print("\n# -----------------------------")
print("# 1. WHAT input() RETURNS")
print("# -----------------------------\n")

# input() waits for user text and returns it unchanged as a string.
# Even if digits are provided, the type is still str until converted manually.
token = input("Type any text (Python echoes it back): ")
print(f"You entered {token!r}. Type is {type(token).__name__}.")


print("\n# -----------------------------")
print("# 2. PROMPTS & WHITESPACE")
print("# -----------------------------\n")

# Provide a prompt string to guide the user. The newline is emitted after Enter is pressed.
favorite_food = input("Favorite food? ")
print(f"Delicious! We'll remember {favorite_food}.")

# input() automatically strips the trailing newline but keeps other whitespace.
spacey = input("Type something with spaces at the ends: ")
print(f"Raw capture: {spacey!r}")
print(f"Using strip(): {spacey.strip()!r}")


print("\n# -----------------------------")
print("# 3. CONVERTING TO NUMBERS")
print("# -----------------------------\n")

# Convert with int() or float() depending on the expected numeric type.
years_text = input("How many years have you coded? (digits) ")
try:
    years = int(years_text)
    print(f"In dog years of coding, that's {years * 7}!")
except ValueError:
    print("Couldn't convert to int(); please type digits only next time.")

height_text = input("Height in meters (use decimal point): ")
try:
    height = float(height_text)
    print(f"Height in centimeters: {height * 100:.1f} cm")
except ValueError:
    print("float() failed — decimals require digits and an optional dot.")


print("\n# -----------------------------")
print("# 4. MULTIPLE VALUES IN ONE LINE")
print("# -----------------------------\n")

print("Example: enter width and height separated by spaces (e.g., '3.5 4.2').")
dimensions = input("Dimensions: ").split()
if len(dimensions) == 2: # unpacking
    width_text, height_text = dimensions # unpacking
    try:
        width = float(width_text)
        height = float(height_text)
        area = width * height
        diag = math.hypot(width, height)
        print(f"Rectangle area = {area:.2f}; diagonal ≈ {diag:.2f}")
    except ValueError:
        print("Could not convert one of the values to float.")
else:
    print("Tip: provide exactly two numbers next time.")


print("\n# -----------------------------")
print("# 5. TRY/EXCEPT LOOP FOR CLEAN INPUT")
print("# -----------------------------\n")

# When validating, loop until the user supplies something acceptable.
while True:
    price_text = input("Enter a ticket price (USD): ")
    try:
        ticket_price = float(price_text)
        if ticket_price <= 0:
            print("Ticket price must be positive.")
            continue
        print(f"Ticket accepted at ${ticket_price:.2f}")
        break
    except ValueError:
        print("Please type a valid number. Example: 19.99")


print("\n# -----------------------------")
print("# 6. MINI PRACTICE")
print("# -----------------------------\n")

# Practice 1 — greet the user.
visitor = input("Your name: ")
city = input("City you want to visit: ")
print(f"Welcome, {visitor}! Planning a trip to {city} sounds fun.\n")

# Practice 2 — simple average calculator.
print("Enter three exam scores separated by spaces (e.g., '78 82 90').")
scores_line = input("Scores: ")
parts = scores_line.split()
if len(parts) == 3:
    try:
        scores = [float(p) for p in parts]
        average = sum(scores) / len(scores)
        print(f"Average score = {average:.1f}")
    except ValueError:
        print("Looks like one score was not numeric.")
else:
    print("Need exactly three numbers for the average.")

# Practice 3 — multi-step prompt and conversion.
bill_text = input("\nRestaurant bill total: ")
people_text = input("Number of people splitting the bill: ")
try:
    bill_total = float(bill_text)
    people = int(people_text)
    shared = bill_total / people
    print(f"Each person pays ${shared:.2f}")
except (ValueError, ZeroDivisionError):
    print("Provide numeric values and ensure number of people is not zero.")


print("\ninput() adventures complete! Rerun this file anytime to practice again.")
