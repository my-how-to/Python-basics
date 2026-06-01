# ============================================================
#            LESSON — THE CSV.READER FUNCTION
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from Google Gemini)
#
# Description:
#   This lesson explains the csv.reader function in Python: 
#   what it is, basic syntax, differences from standard 
#   file reading methods, and practical data processing.
#
# Contents:
#   1. What is csv.reader?
#   2. Basic syntax and context managers (with open)
#   3. csv.reader vs .split(",")
#   4. Handling headers with next()
#   5. Data types: Why everything is a string
#   6. Custom delimiters (delimiter=";")
#   7. Practical mini-examples
# ============================================================

import csv

# ------------------------------------------------------------
# 1. WHAT IS CSV.READER?
# ------------------------------------------------------------
# csv.reader is a built-in Python tool used to read text files
# line by line, automatically parsing commas (or other marks)
# into organized Python lists.


print("\n------------------------------------------------------------")
print("2. BASIC SYNTAX & CONTEXT MANAGERS")
print("------------------------------------------------------------\n")

# Always use 'newline=""' and 'encoding="utf-8"' as a best practice.

# Let's create a temporary file first
with open("test.csv", "w", newline="", encoding="utf-8") as f:
    f.write("name,age\nAlice,25\nBob,30")

# Reading the file
with open("test.csv", "r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)  # Creates the reader object
    for row in csv_reader:
        print(row)  # Each row is a list of strings


# ------------------------------------------------------------
# 3. CSV.READER VS .SPLIT(",")
# ------------------------------------------------------------
# Standard text .split(",") breaks if data contains commas inside 
# quotes, e.g., "Smith, John". csv.reader handles this correctly.


print("\n------------------------------------------------------------")
print("4. HANDLING HEADERS WITH NEXT()")
print("------------------------------------------------------------\n")

with open("test.csv", "r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Grabs the first row
    print("Headers extracted:", headers)
    print("Remaining data rows:")
    for row in csv_reader:
        print(row)


# ------------------------------------------------------------
# 5. DATA TYPES: EVERYTHING IS A STRING
# ------------------------------------------------------------
# csv.reader reads numbers as text. You must convert integers 
# using int() and decimals using float() before doing math.


print("\n------------------------------------------------------------")
print("6. CUSTOM DELIMITERS (delimiter=\";\")")
print("------------------------------------------------------------\n")

# Creating a semicolon separated file
with open("semi.csv", "w", newline="", encoding="utf-8") as f:
    f.write("product;price\nMilk;2.20")

with open("semi.csv", "r", newline="", encoding="utf-8") as file:
    # Tell the reader to look for semicolons instead of commas
    csv_reader = csv.reader(file, delimiter=";")
    next(csv_reader)
    for row in csv_reader:
        print(row)


print("\n------------------------------------------------------------")
print("7. PRACTICAL MINI-EXAMPLES")
print("------------------------------------------------------------\n")

# Let's sum up all ages from the test.csv file
data_summary = 0
with open("test.csv", "r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip "name,age"
    for row in csv_reader:
        data_summary += int(row[1])  # Sum up all ages

print(f"Sum of all ages in file: {data_summary}")
