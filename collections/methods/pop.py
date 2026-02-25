# ==========================================================
#               pop()
# ==========================================================
#
# 1) WHAT IS pop()?
#
# pop() removes and RETURNS an element from a collection.
#
# It modifies the collection in-place.
#
# Return value:
# - list → removed element
# - dict → removed value
# - set  → removed element
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.pop()
# list.pop(index)
#
# dict.pop(key)
# dict.pop(key, default)
#
# set.pop()
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available on:
# - list
# - dict
# - set
#
# Not available on:
# - tuple (immutable)
# - str (immutable)
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# LIST VERSION (conceptual):
#
# def pop(self, index=-1):
#     value = self[index]
#     del self[index]
#     return value
#
#
# DICT VERSION (conceptual):
#
# def pop(self, key):
#     value = self[key]
#     del self[key]
#     return value
#
#
# Key ideas:
# - Removes element
# - Returns removed value
# - Raises error if key/index invalid (unless default provided in dict)
#
# ==========================================================
# 5) LIST EXAMPLES
# ==========================================================

numbers = [10, 20, 30, 40]

print(numbers.pop())
# Output: 40  (removes last element)

print(numbers)
# [10, 20, 30]

print(numbers.pop(1))
# Output: 20  (removes element at index 1)

print(numbers)
# [10, 30]


# ==========================================================
# 6) DICTIONARY EXAMPLES
# ==========================================================

d = {"a": 1, "b": 2}

print(d.pop("a"))
# Output: 1

print(d)
# {'b': 2}

# With default (prevents KeyError)

print(d.pop("x", 0))
# Output: 0


# ==========================================================
# 7) SET EXAMPLE
# ==========================================================

s = {1, 2, 3}

removed = s.pop()

print(removed)
# Removes arbitrary element (sets are unordered)

print(s)


# ==========================================================
# 8) ERROR CASES
# ==========================================================

lst = [1, 2, 3]

# lst.pop(10)
# Raises IndexError

d = {"a": 1}

# d.pop("b")
# Raises KeyError


# ==========================================================
# 9) pop() VS remove() VS del
# ==========================================================
#
# pop(index)
#   - Removes by INDEX
#   - Returns removed value
#
# remove(value)
#   - Removes by VALUE
#   - Returns None
#
# del list[index]
#   - Removes by INDEX
#   - Does NOT return value
#
# ==========================================================
# 10) TIME COMPLEXITY
# ==========================================================
#
# list.pop()      → O(1)  (last element)
# list.pop(index) → O(n)  (shift elements)
# dict.pop(key)   → O(1) average
# set.pop()       → O(1) average
#
# ==========================================================
# 11) KEY RULES
# ==========================================================
#
# - pop() removes AND returns.
# - Modifies collection in-place.
# - list default removes last element.
# - dict.pop() can accept default value.
# - set.pop() removes arbitrary element.
#
# ==========================================================
# END OF LESSON
# ==========================================================
