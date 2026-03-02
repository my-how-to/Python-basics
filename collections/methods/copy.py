# ==========================================================
#               copy()
# ==========================================================
#
# 1) WHAT IS copy()?
#
# copy() creates a SHALLOW COPY of a collection.
#
# It returns a new object with the same elements.
#
# Return value:
# - New collection object
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# collection.copy()
#
# No arguments.
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
# - tuple (immutable; use tuple() or slicing)
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation for list:
#
# def copy(self):
#     new_list = []
#     for element in self:
#         new_list.append(element)
#     return new_list
#
# Key idea:
# - Creates a new outer container
# - Elements are NOT deeply copied
#
# This is called a SHALLOW COPY.
#
# Time complexity: O(n)
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- LIST COPY ----------

a = [1, 2, 3]
b = a.copy()

print(b)
# Output: [1, 2, 3]

print(a is b)
# Output: False  (different objects)


# ---------- DICT COPY ----------

d1 = {"x": 1, "y": 2}
d2 = d1.copy()

print(d2)
# Output: {'x': 1, 'y': 2}

print(d1 is d2)
# Output: False


# ---------- SET COPY ----------

s1 = {1, 2, 3}
s2 = s1.copy()

print(s2)
# Output: {1, 2, 3}


# ==========================================================
# 6) IMPORTANT BEHAVIOR (SHALLOW COPY WARNING)
# ==========================================================
#
# Nested objects are NOT copied.

a = [[1, 2], [3, 4]]
b = a.copy()

b[0][0] = 999

print(a)
# Output: [[999, 2], [3, 4]]
#
# Because inner lists are shared references.


# ==========================================================
# 7) copy() vs DEEP COPY
# ==========================================================
#
# copy() → shallow copy
#
# For deep copy use:
#
# import copy
# copy.deepcopy(object)
#
# deepcopy() copies nested objects as well.
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================
#
# ❌ b = a
#    This does NOT copy.
#    It creates another reference.
#
# ✔ Correct:
#    b = a.copy()
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - Returns new object.
# - Shallow copy only.
# - O(n) time.
# - Available on list, dict, set.
#
# ==========================================================
# END OF LESSON
# ==========================================================