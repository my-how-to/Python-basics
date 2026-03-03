# ==========================================================
#               map()
# ==========================================================
#
# 1) WHAT IS map()?
#
# map() applies a function to every element of an iterable.
#
# It returns an iterator with transformed values.
#
# Return value:
# - map object (iterator)
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# map(function, iterable)
#
# function  → applied to each element
# iterable  → list, tuple, set, etc.
#
# Optional:
# map(function, iterable1, iterable2, ...)
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
# def map(function, iterable):
#     for element in iterable:
#         yield function(element)
#
# Key idea:
# - Lazy evaluation (values generated on demand)
# - Does NOT store results immediately
# - Memory efficient
# - Time complexity: O(n) for n elements in the iterable. 
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- SIMPLE TRANSFORMATION ----------

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
# Output: [2, 4, 6, 8]


# ---------- CONVERTING TYPES ----------

nums = ["1", "2", "3"]

converted = map(int, nums)

print(list(converted))
# Output: [1, 2, 3]


# ---------- MULTIPLE ITERABLES ----------

a = [1, 2, 3]
b = [10, 20, 30]

result = map(lambda x, y: x + y, a, b)

print(list(result))
# Output: [11, 22, 33]


# ==========================================================
# 6) IMPORTANT BEHAVIOR
# ==========================================================
#
# map() returns an iterator.
#
# Once consumed, it is exhausted.

nums = [1, 2, 3]

m = map(lambda x: x + 1, nums)

print(list(m))  # [2, 3, 4]
print(list(m))  # []  (already consumed)


# ==========================================================
# 7) map() vs LIST COMPREHENSION
# ==========================================================
#
# map():
#     map(lambda x: x*2, nums)
#
# List comprehension:
#     [x*2 for x in nums]
#
# List comprehension is often more readable.
# map() is useful when:
# - Passing an existing function
# - Functional programming style
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================
#
# ❌ print(map(lambda x: x*2, [1,2,3]))
#    Shows map object, not values.
#
# ✔ Correct:
#    print(list(map(lambda x: x*2, [1,2,3])))
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - Built-in function.
# - Returns iterator.
# - Lazy evaluation.
# - Works with one or multiple iterables.
# - O(n) time complexity.
#
# ==========================================================
# END OF LESSON
# ==========================================================