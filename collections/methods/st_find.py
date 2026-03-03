# ==========================================================
#               find()
# ==========================================================
#
# 1) WHAT IS find()?
#
# find() searches for a substring inside a string.
#
# It returns the index of the FIRST occurrence of the substring.
#
# If the substring is NOT found, it returns -1.
#
# Return value:
# - integer (index)
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# string.find(substring, start, end)
#
# substring → text to search for
# start     → optional start index
# end       → optional end index
#
# Only substring is required.
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available on:
# - str
#
# Not available on:
# - list
# - tuple
# - set
# - dict
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Conceptual implementation:
#
# def find(text, substring):
#     for i in range(len(text)):
#         if text[i:i+len(substring)] == substring:
#             return i
#     return -1
#
# Key idea:
# - Scans the string from left to right
# - Returns first match
# - Returns -1 if no match
#
# Time complexity: O(n)
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- SIMPLE SEARCH ----------

text = "Python programming"

print(text.find("prog"))
# Output: 7


# ---------- NOT FOUND ----------

text = "Python"

print(text.find("Java"))
# Output: -1


# ---------- USING START POSITION ----------

text = "banana"

print(text.find("na", 3))
# Output: 4


# ---------- USING START AND END ----------

text = "banana"

print(text.find("na", 0, 4))
# Output: 2


# ==========================================================
# 6) IMPORTANT BEHAVIOR
# ==========================================================
#
# find() returns -1 if substring is missing.
#
# This allows safe checks:

text = "Python"

if text.find("th") != -1:
    print("Found")


# ==========================================================
# 7) find() vs index()
# ==========================================================
#
# find()
#     returns -1 if not found
#
# index()
#     raises ValueError if not found
#
# Example:
#
# "abc".find("x")   → -1
# "abc".index("x")  → ValueError
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================
#
# ❌ if text.find("word"):
#    This may fail if index is 0
#
# ✔ Correct:
#
# if text.find("word") != -1:
#     ...
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - String method.
# - Returns index of first match.
# - Returns -1 if not found.
# - Optional start and end range.
# - O(n) time complexity.
#
# ==========================================================
# END OF LESSON
# ==========================================================