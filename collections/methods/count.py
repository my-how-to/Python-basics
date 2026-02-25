# ==========================================================
#               count()
# ==========================================================
#
# 1) WHAT IS count()?
#
# count() returns the number of occurrences of a value inside a collection.
#
# It does NOT modify the collection.
#
# Return value: int
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.count(value)
# tuple.count(value)
#
# str.count(substring)
# str.count(substring, start)
# str.count(substring, start, end)
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available on:
# - list
# - tuple
# - str
#
# Not available on:
# - set (unordered, no duplicates)
# - dict (no count() method)
#
# ==========================================================
# 4) ARGUMENT DIFFERENCES BY TYPE
# ==========================================================
#
# LIST / TUPLE:
#   Accept EXACTLY ONE argument.
#
#   numbers.count(2)
#
#   numbers.count(2, 1)  → TypeError
#
#
# STRING:
#   Accepts 1–3 arguments.
#
#   text.count("a")
#   text.count("a", start)
#   text.count("a", start, end)
#
#   start → inclusive
#   end   → exclusive
#
# ==========================================================
# 5) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation for list:
#
# def count(self, value):
#     counter = 0
#     for element in self:
#         if element == value:
#             counter += 1
#     return counter
#
# Key idea:
# - Linear scan
# - Time complexity: O(n)
#
# For strings:
# - Searches for substring occurrences
# - Can restrict range with start/end
#
# ==========================================================
# 6) BASIC EXAMPLES
# ==========================================================

# ---------- LIST ----------

numbers = [1, 2, 3, 2, 2, 4]

print(numbers.count(2))
# Output: 3


# ---------- TUPLE ----------

data = (10, 20, 10, 30)

print(data.count(10))
# Output: 2


# ---------- STRING ----------

text = "banana"

print(text.count("a"))
# Output: 3

print(text.count("a", 2))
# Output: 2

print(text.count("a", 2, 5))
# Output: 1


# ==========================================================
# 7) RANGE WORKAROUND FOR LISTS
# ==========================================================
#
# Lists do NOT support start/end arguments.
# You must slice manually:
#

numbers = [1, 2, 2, 3, 2, 4]

print(numbers[1:5].count(2))
# Output: 2


# ==========================================================
# 8) IMPORTANT BEHAVIOR
# ==========================================================
#
# count() uses equality (==), not identity (is)
#

class A:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

a1 = A(10)
a2 = A(10)

lst = [a1]

print(lst.count(a2))
# Output: 1


# ==========================================================
# 9) DICTIONARY NOTE
# ==========================================================
#
# Dictionaries do not have count().
#
# To count values:
#
# d = {"a": 1, "b": 1, "c": 2}
#
# print(list(d.values()).count(1))
# Output: 2
#
# ==========================================================
# 10) KEY RULES
# ==========================================================
#
# - Returns number of occurrences.
# - Does NOT modify collection.
# - list/tuple → exactly 1 argument.
# - str → supports start and end.
# - Time complexity O(n).
# - Uses equality comparison (==).
#
# ==========================================================
# END OF LESSON
# ==========================================================
