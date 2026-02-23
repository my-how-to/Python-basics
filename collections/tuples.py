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
print(type(singleton)) # <class 'tuple'> - the comma is what makes it a tuple, not the parentheses.

# ------------------------------------------------------------
# Looping
# ------------------------------------------------------------
# The for-loop is designed for iterating sequences and other iterables.
for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------
# Immutability
# ------------------------------------------------------------
# fruits[1] = "orange"  # TypeError! Tuples do not support item assignment because they are immutable.
# To "modify" a tuple, create a new one:
new_fruits = fruits[:1] + ("orange",) + fruits[2:]
print(new_fruits)  # ('apple', 'orange', 'cherry')

# you can modify mutable elements inside a tuple, but not the tuple itself:
app_data = (1, 2, ["start", "end"]) 
# app_data[2] = ["stop", "end"]  # TypeError! Cannot reassign the entire list at index 2 because the tuple is immutable.
app_data[2][0] = "stop" # This works because we're modifying the list inside the tuple, not the tuple itself.
print(app_data) # (1, 2, ['stop', 'end']) - the tuple is unchanged, but the list inside it is modified.

# This is a common pitfall: if you have mutable objects (like lists) inside a tuple, 
# you can modify those mutable objects, but you cannot change the structure of the tuple itself.
box = (1, [10, 20], 3)
box[1].sort(reverse=True)
print(box) # (1, [20, 10], 3) - the tuple itself is unchanged, but the list inside it is modified in place.

box[1].append(5)
print(box) # (1, [20, 10, 5], 3) - again, the tuple is unchanged, but the list inside it is modified.



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

vals = (10, 20, 30)
a, *b = vals
print(type(a)) # 10         <class 'int'>   - a is assigned the first value, which is an integer.
print(type(b)) # [20, 30]   <class 'list'>  - b is assigned the remaining values as a list because of the * operator.

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
#
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
# index() has an optional start parameter to specify where to begin the search.

print(marks.index("B"))  # 1
print(marks.index("A", 1))  # 2 - starts searching for "A" from index 1, so it finds the second "A" at index 2.

#
# If the value is not found, it raises a ValueError.
# why not use 'in' to check existence first?
# It's more efficient to use index() directly if you know the value exists.
# Using 'in' would require two passes: one to check existence and another to find the index.
# Using index() directly performs a single pass.
#
# index() only returns the first occurrence, so if you need all positions, you'd have to loop through the tuple.
animals = ("cat", "dog", "cat")
print(animals.index("cat"))  # 0

# ------------------------------------------------------------
# sorted()
# ------------------------------------------------------------
# sorted() returns a new list of sorted elements from the tuple.
# sorted() has optional parameters like reverse=True for descending order and key for custom sorting.

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

# Slicing a tuple that results in a single element still returns a tuple if you use the comma.
tup = ([],) * 2
tup[0].append(1)
print(tup) # ([1], [1]) - both elements refer to the same list object, so modifying one modifies the other. This is a common pitfall when using mutable objects inside tuples.


print("\n# -----------------------------")
print("# 3. Tuple Concatenation")
print("# -----------------------------\n")

# Tuples can be joined using +
a = (1, 2, 3)
b = (4, 5)
print(a + b)  # (1, 2, 3, 4, 5)

# Tuples can also be repeated using *
print(a * 2)  # (1, 2, 3, 1, 2, 3)

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