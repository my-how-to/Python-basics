# ==========================================================
#               Built-in Function: sorted()
# ==========================================================
#
# 1) WHAT IS sorted()?
#
# sorted() is a built-in function that returns
# a NEW sorted list from any iterable.
#
# It does NOT modify the original object.
#
# Return type: list
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# sorted(iterable)
# sorted(iterable, key=...)
# sorted(iterable, reverse=True/False)
#
# iterable → any iterable object
# key      → function used for custom sorting
# reverse  → if True, sorts descending
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Works with:
# - list
# - tuple
# - set
# - dict (sorts keys)
# - str
# - any iterable
#
# Important:
# Always returns a LIST.
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Python uses Timsort algorithm:
# - Hybrid of merge sort and insertion sort
# - Stable sort (preserves order of equal elements)
# - Time complexity: O(n log n)
#
# Conceptually:
#
# def sorted(iterable):
#     temp_list = list(iterable)
#     temp_list.sort()
#     return temp_list
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- LIST ----------

numbers = [4, 1, 3, 2]

result = sorted(numbers)

print(result)
# Output: [1, 2, 3, 4]

print(numbers)
# Original unchanged: [4, 1, 3, 2]


# ---------- TUPLE ----------

t = (5, 2, 8, 1)

print(sorted(t))
# Output: [1, 2, 5, 8]


# ---------- SET ----------

s = {3, 1, 4, 2}

print(sorted(s))
# Output: [1, 2, 3, 4]


# ---------- DICTIONARY ----------

d = {"b": 2, "a": 1, "c": 3}

print(sorted(d))
# Output: ['a', 'b', 'c']
# Sorted by KEYS


# ---------- STRING ----------

text = "dcba"

print(sorted(text))
# Output: ['a', 'b', 'c', 'd']


# ==========================================================
# 6) reverse PARAMETER
# ==========================================================

numbers = [1, 4, 2, 3]

print(sorted(numbers, reverse=True))
# Output: [4, 3, 2, 1]


# ==========================================================
# 7) key PARAMETER (VERY IMPORTANT)
# ==========================================================

# Sort by length

words = ["apple", "kiwi", "banana"]

print(sorted(words, key=len))
# Output: ['kiwi', 'apple', 'banana']


# Sort by last digit
# Note: x % 10 gives the last digit of a number. 

numbers = [21, 34, 12, 45]

print(sorted(numbers, key=lambda x: x % 10))
# Output: [21, 12, 34, 45]


# ==========================================================
# 8) sorted() VS list.sort()
# ==========================================================
#
# sorted(iterable)
#   - Returns new list
#   - Works on any iterable
#   - Does NOT modify original
#
# list.sort()
#   - Works only on lists
#   - Modifies list in-place
#   - Returns None
#
# Example:

numbers = [3, 1, 2]

numbers.sort()

print(numbers)
# Output: [1, 2, 3]


# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - Always returns a new LIST.
# - Does NOT modify original iterable.
# - Uses stable sorting (Timsort).
# - Time complexity O(n log n).
# - Supports key and reverse parameters.
#
# ==========================================================
# END OF LESSON
# ==========================================================
