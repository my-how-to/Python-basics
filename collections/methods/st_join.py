# ==========================================================
#               join()
# ==========================================================
#
# 1) WHAT IS join()?
#
# join() concatenates elements of an iterable into ONE string,
# using the string it is called on as a separator.
#
# It does NOT modify the original iterable.
#
# Return value:
# - New string
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# separator.join(iterable)
#
# separator → string used between elements
# iterable  → must contain ONLY strings
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# join() is a STRING method.
#
# It works with iterables like:
# - list of strings
# - tuple of strings
# - set of strings
#
# It does NOT work if elements are not strings.
#
# Example:
# ",".join([1, 2, 3])  → TypeError
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Conceptually:
#
# def join(self, iterable):
#     result = ""
#     for element in iterable:
#         result += element + self
#     remove_last_separator()
#     return result
#
# Real implementation is optimized in C.
#
# Key idea:
# - Efficient string concatenation
# - Time complexity: O(n)
# - Much faster than repeated "+"
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- SIMPLE JOIN ----------

words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)
# Output: Python is powerful


# ---------- CUSTOM SEPARATOR ----------

numbers = ["1", "2", "3"]

result = "-".join(numbers)

print(result)
# Output: 1-2-3


# ---------- JOIN WITH TUPLE ----------

t = ("A", "B", "C")

print(",".join(t))
# Output: A,B,C


# ==========================================================
# 6) IMPORTANT BEHAVIOR
# ==========================================================
#
# All elements must be strings.
#
# Example:

data = ["Age:", 30]

# ",".join(data)  → TypeError

# Correct way:
print(",".join(map(str, data)))
# Output: Age:,30


# ==========================================================
# 7) join() vs "+"
# ==========================================================
#
# ❌ Inefficient:
#
# s = ""
# for word in words:
#     s += word
#
# ✔ Efficient:
#
# " ".join(words)
#
# join() is optimized and faster for many strings.
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================
#
# ❌ words.join(" ")
#    Wrong order.
#
# ✔ Correct:
#    " ".join(words)
#
# The separator comes FIRST.
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - String method.
# - Returns new string.
# - Does NOT modify original iterable.
# - Elements must be strings.
# - O(n) time complexity.
#
# ==========================================================
# END OF LESSON
# ==========================================================