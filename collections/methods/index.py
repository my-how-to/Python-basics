# ==========================================================
#               index()
# ==========================================================
#
# 1) WHAT IS index()?
#
# index() searches for a value and returns the position (index) of its FIRST occurrence.
#
# If the value is not found → raises ValueError.
#
# Return type: int
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# sequence.index(value)
# sequence.index(value, start)
# sequence.index(value, start, end)
#
# value  → element to search for
# start  → optional starting index
# end    → optional ending index (exclusive)
#
# Works only on SEQUENCES.
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available on:
# - list
# - tuple
# - string
#
# Not available on:
# - set (unordered)
# - dict (no positional indexing)
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation:
#
# def index(self, value, start=0, end=len(self)):
#     for i in range(start, end):
#         if self[i] == value:
#             return i
#     raise ValueError("value not found")
#
# Key idea:
# - Linear search (O(n))
# - Stops at first match
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- LIST ----------

numbers = [10, 20, 30, 20]

print(numbers.index(20))
# Output: 1 (first occurrence only)

print(numbers.index(20, 2))
# Output: 3 (search starting from index 2)


# ---------- TUPLE ----------

t = (5, 6, 7, 6)

print(t.index(6))
# Output: 1


# ---------- STRING ----------

text = "banana"

print(text.index("a"))
# Output: 1

print(text.index("a", 2))
# Output: 3


# ==========================================================
# 6) ERROR CASE
# ==========================================================

values = [1, 2, 3]

# values.index(5)
# Raises:
# ValueError: 5 is not in list


# ==========================================================
# 7) DIFFERENCE BETWEEN index() AND find() (strings)
# ==========================================================
#
# string.index(substring)
#     → Raises ValueError if not found
#
# string.find(substring)
#     → Returns -1 if not found
#
# index() is stricter.
#
# ==========================================================
# 8) IMPORTANT RULES
# ==========================================================
#
# - Returns FIRST occurrence only.
# - Raises ValueError if not found.
# - Uses linear search (O(n)).
# - Works only on ordered sequences.
#
# ==========================================================
# END OF LESSON
# ==========================================================
