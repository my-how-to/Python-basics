# ============================================================
#            LESSON - TUPLES (COLLECTIONS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson covers tuples in Python: what they are, how to
#   create them, indexing and slicing, immutability, tuple
#   unpacking, single-element tuples, and tuple concatenation.
#
# Why use tuples?
# * Faster and lighter than lists.
# * Ideal for fixed datasets (coordinates, weekdays, etc.).
# * Can serve as dictionary keys or set members.
# * Enable multiple return values from functions.
# * Support unpacking for easy variable assignment.
#
# Contents:
#   1. Tuples — Immutable Sequences
#   2. Tuple Tricks
#     - count()
#     - index()
#     - sorted()
#   3. Tuple Concatenation  
#  
print("\n# -----------------------------")
print("# 1. Tuples — Immutable Sequences")
print("# -----------------------------\n")

fruits = ("apple", "banana", "cherry")
print(fruits[0])  # apple

# ------------------------------------------------------------
# Tuples without parentheses
# ------------------------------------------------------------
# Parentheses are optional when commas are present.
colors = "red", "green", "blue"
print(colors)

singleton = "only_one",
print(type(singleton))

# ------------------------------------------------------------
# Looping
# ------------------------------------------------------------
# The for-loop is designed for iterating sequences and other iterables.
for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------
# Immutability
# ------------------------------------------------------------
# fruits[1] = "orange"  # Error! Tuples are immutable
# To "modify" a tuple, create a new one:
new_fruits = fruits[:1] + ("orange",) + fruits[2:]
print(new_fruits)  # ('apple', 'orange', 'cherry')

# you can modify mutable elements inside a tuple, but not the tuple itself:
app_data = (1, 2, ["start", "end"]) # app_data[2] = ["stop", "end"]  # Error! Can't change the tuple's structure
app_data[2][0] = "stop" # This works because we're modifying the list inside the tuple, not the tuple itself.
print(app_data) # (1, 2, ['stop', 'end']) - the tuple is unchanged, but the list inside it is modified.

print("\n# -----------------------------")
print("# 2. Tuple Tricks")
print("# -----------------------------\n")

# ------------------------------------------------------------
# Single-element tuple
# ------------------------------------------------------------
t = ("apple",)
print(type(t)) # <class 'tuple'>

single_val = (50) # This is just an integer, not a tuple!
print(type(single_val)) # <class 'int'> - not a tuple!

# ------------------------------------------------------------
# tuple() constructor
# ------------------------------------------------------------
# tuple() converts other iterables into tuples.
letters = tuple("ABC")
print(letters)  # ('A', 'B', 'C')

nums = tuple([1, 2, 3])
print(nums)  # (1, 2, 3)

# ------------------------------------------------------------
# Tuple unpacking
# ------------------------------------------------------------
person = ("Alex", 32, "Moldova")
name, age, country = person
print(name, age, country) # Alex 32 Moldova
print("See /assignments/multiple_assignment.py for advanced packing/unpacking patterns.")

# ------------------------------------------------------------
# Swapping tuple values (unpacking)
# ------------------------------------------------------------
# Tuple unpacking lets you swap values without a temporary variable.
# why use tuples for swapping?
# It provides a concise and readable way to swap values in a single line.
# Using a temporary variable would require three lines and be less clear.
left = (1,)
middle = (2,)
right = (3,)

left, middle, right = middle, right, left
print(left, middle, right) # (2,) (3,) (1,)

vals = (10, 20, 30) 
# to swap the first two values, we can unpack and reassign them in one line:
vals[0], vals[1] = vals[1], vals[0] # This creates a new tuple with the swapped values and assigns it back to vals.
print(vals) # (20, 10, 30) - values swapped, but the tuple itself is unchanged (a new tuple is created)

# ------------------------------------------------------------
# Variables inside tuples
# ------------------------------------------------------------
# Tuples can store variables as elements.
# This is useful for grouping related data.

level = 42
badge = (3, level)
print(badge) # (3, 42)

# ------------------------------------------------------------
# count() method
# ------------------------------------------------------------
# count() returns how many times a value appears in the tuple.
# why not use 'in' to check existence first?
# It's more efficient to use count() directly if you need the count.
# Using 'in' would require two passes: one to check existence and another to count.
# Using count() directly performs a single pass.
marks = ("A", "B", "A", "C", "A")
print(marks.count("A"))  # 3

# ------------------------------------------------------------
# index() method
# ------------------------------------------------------------
# index() searches for a value and returns its position.
# If the value is not found, it raises a ValueError.
# why not use 'in' to check existence first?
# It's more efficient to use index() directly if you know the value exists.
# Using 'in' would require two passes: one to check existence and another to find the index.
# Using index() directly performs a single pass.
# index() only returns the first occurrence, so if you need all positions, you'd have to loop through the tuple.
animals = ("cat", "dog", "cat")
print(animals.index("cat"))  # 0

# ------------------------------------------------------------
# sorted()
# ------------------------------------------------------------
# sorted() returns a new list of sorted elements from the tuple.
# why use sorted() instead of sort()?
# sorted() works on any iterable and returns a new sorted list, while sort() is a
# method that modifies a list in place and can only be used on lists.
numbers = (3, 1, 2)
sorted_numbers = sorted(numbers)
print("sorted() returns a list ", sorted_numbers, type(sorted_numbers))  # [1, 2, 3] - sorted() returns a new list, not a tuple. If you want a sorted tuple, you can convert it back
sorted_tuple = tuple(sorted_numbers)
print(sorted_tuple), type(sorted_numbers) # (1, 2, 3) - now we have a sorted tuple.

# ------------------------------------------------------------
# Tuples slicing
# ------------------------------------------------------------

# Slicing works the same as with lists, but it returns a new tuple.
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4], type(numbers))  # (20, 30, 40) <class 'tuple'>

versions = (1.0, 1.1, 1.2, 1.3)
subset = versions[1:2]
print(subset) # (1.1,) - still a tuple, even with one element, because of the comma.


print("\n# -----------------------------")
print("# 3. Tuple Concatenation")
print("# -----------------------------\n")

# Tuples can be joined using +
a = (1, 2, 3)
b = (4, 5)
print(a + b)  # (1, 2, 3, 4, 5)

cfg_params = (1024, "admin", "v1")
cfg_params[1] = "root"
print(cfg_params) #


# ------------------------------------------------------------
# Tuples Сomparison
# ------------------------------------------------------------
# Tuples are compared element-wise, starting from the first element.
# The first pair of elements that differ determine the outcome of the comparison.
# If all elements are equal, the tuples are considered equal.
print((1, 2, 3) == (1, 2, 3)) # True
print((1, 2, 3) == (1, 2, 4)) # False   
print((1, 2, 3) < (1, 2, 4)) # True - because the first two elements are equal, but the third element (3) is less than 4.
print((1, 2) < (1, 2, 0)) # True - because the first two elements are equal, but the first tuple has fewer elements than the second, so it's considered less than the second tuple.

# Tuples comparisons are useful for sorting and ordering data, 
# as they allow you to compare complex structures in a straightforward way.