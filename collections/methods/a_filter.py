# ==========================================================
#                       filter()
# ==========================================================
#
# 1) WHAT IS filter()?
#
# filter() selects elements from an iterable
# for which a function returns True.
#
# It returns an iterator containing only
# the elements that satisfy the condition.
#
# Return value:
# - filter object (iterator)
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# filter(function, iterable)
#
# function  → must return True or False
# iterable  → any iterable (list, tuple, set, etc.)
#
# Special case:
# filter(None, iterable)
# → removes falsy values
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Works with any iterable:
# - list
# - tuple
# - set
# - range
# - string
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Conceptually:
#
# def filter(function, iterable):
#     for element in iterable:
#         if function(element) is True:
#             yield element
#
# Key idea:
# - Lazy evaluation (values produced on demand)
# - Does NOT create a list automatically
# - Memory efficient
# - Time complexity: O(n)
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- FILTER EVEN NUMBERS ----------

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
# Output: [2, 4, 6]


# ---------- FILTER POSITIVE NUMBERS ----------

nums = [-3, -1, 0, 2, 4]

positive = filter(lambda x: x > 0, nums)

print(list(positive))
# Output: [2, 4]


# ==========================================================
# 6) filter(None, iterable)
# ==========================================================
#
# Removes falsy values:
# - 0
# - False
# - None
# - ""
# - []
# - {}

data = [0, 1, "", "hello", None, 5]

cleaned = filter(None, data)

print(list(cleaned))
# Output: [1, 'hello', 5]


# ==========================================================
# 7) IMPORTANT BEHAVIOR
# ==========================================================
#
# filter() returns an iterator.
# It is consumed once.

nums = [1, 2, 3]

f = filter(lambda x: x > 1, nums)

print(list(f))  # [2, 3]
print(list(f))  # []  (already consumed)


# ==========================================================
# 8) filter() vs LIST COMPREHENSION
# ==========================================================
#
# filter():
#     filter(lambda x: x > 0, nums)
#
# List comprehension:
#     [x for x in nums if x > 0]
#
# List comprehension is often more readable.
# filter() is useful in functional programming style.
#
# ==========================================================
# 9) COMMON MISTAKE
# ==========================================================
#
# ❌ print(filter(lambda x: x > 0, [1,2,3]))
#    Shows filter object, not values.
#
# ✔ Correct:
#    print(list(filter(lambda x: x > 0, [1,2,3])))
#
# ==========================================================
# 10) KEY RULES
# ==========================================================
#
# - Built-in function.
# - Returns iterator.
# - Keeps elements where function returns True.
# - Lazy evaluation.
# - O(n) time complexity.
#
# ==========================================================
# END OF LESSON
# ==========================================================