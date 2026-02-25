# ==========================================================
#               Function: len()
# ==========================================================
#
# 1) WHAT IS len()?
# len() is a built-in Python function that returns the number
# of elements in a collection.
#
# It internally calls:
# object.__len__()
#
#
# 2) SYNTAX
# len(object)
#
#
# 3) WHERE CAN IT BE USED?
#
# Sequences:
# - list
# - tuple
# - range
# - str
#
# Sets:
# - set
# - frozenset
#
# Mappings:
# - dict  (counts keys)
#
# Binary types:
# - bytes
# - bytearray
#
#
# 4) WHAT DOES IT RETURN?
# Returns an integer (int).
#
# list / tuple / set → number of elements
# dict               → number of keys
# str                → number of characters
# range              → total generated values
#
#
# 5) DOES IT MODIFY THE OBJECT?
# No. len() is read-only.
#
#
# 6) TIME COMPLEXITY
# O(1) for built-in collections.
# Length is stored internally, not recalculated.
#
#
# 7) BASIC EXAMPLES

numbers = [10, 20, 30]
print(len(numbers))        # 3

t = (1, 2, 3, 4)
print(len(t))              # 4

s = {1, 2, 3}
print(len(s))              # 3

d = {"a": 1, "b": 2}
print(len(d))              # 2

text = "Python"
print(len(text))           # 6


#
# 8) CUSTOM OBJECT SUPPORT
# If a class defines __len__(), len() will work on it.

class MyCollection:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

obj = MyCollection([1, 2, 3, 4])
print(len(obj))            # 4


#
# 9) COMMON MISTAKES
#
# ❌ numbers.len()      # WRONG (len is not a method)
# ❌ len(10)            # TypeError (int has no length)
# ✅ len(numbers)       # Correct
#
#
# 10) IMPORTANT NOTE
# len() does NOT count nested elements recursively.
# It counts only top-level items.

nested = [[1, 2], [3, 4]]
print(len(nested))         # 2  (not 4)