# ==========================================================
#               Method: append()
# ==========================================================
#
# 1) WHAT IS append()?
#
# append() adds a SINGLE element to the END of a list.
#
# It modifies the list in-place.
#
# Return value: None
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.append(element)
#
# element → any Python object
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available only on:
# - list
#
# Not available on:
# - tuple (immutable)
# - set (use add())
# - dict (use assignment or update())
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation:
#
# def append(self, element):
#     self[len(self):] = [element]
#
# or conceptually:
#
# place element at index len(self)
# increase list size by 1
#
# Key idea:
# - Amortized O(1) time complexity
# - List may resize internally if capacity is full
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- SIMPLE APPEND ----------

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
# Output: [1, 2, 3, 4]


# ---------- APPENDING DIFFERENT TYPES ----------

data = []

data.append(10)
data.append("hello")
data.append([1, 2])

print(data)
# Output: [10, 'hello', [1, 2]]


# ==========================================================
# 6) IMPORTANT BEHAVIOR
# ==========================================================

# append() adds the element AS-IS

lst = [1, 2]
lst.append([3, 4])

print(lst)
# Output: [1, 2, [3, 4]]
# Notice: the list [3, 4] is added as ONE element


# ==========================================================
# 7) append() vs extend()
# ==========================================================
#
# append(x)
#     → adds x as a single element
#
# extend(iterable)
#     → adds each element of iterable separately
#
# Example:
#
# a = [1, 2]
#
# a.append([3, 4])
# # [1, 2, [3, 4]]
#
# a = [1, 2]
# a.extend([3, 4])
# # [1, 2, 3, 4]
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================

numbers = [1, 2, 3]

result = numbers.append(4)

print(result)
# Output: None
#
# append() modifies in-place and returns None.
# Do NOT assign its result to a variable.
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - Only for lists.
# - Modifies list in-place.
# - Returns None.
# - Adds exactly ONE element.
# - O(1) amortized time.
#
# ==========================================================
# END OF LESSON
# ==========================================================
