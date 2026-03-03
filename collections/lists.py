# ============================================================
#            LESSON — LISTS (COLLECTIONS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson covers lists in Python: what they are, how to
#   create them, accessing and modifying items, useful list
#   methods, looping through lists, list comprehensions, and
#   nested lists.
#   
#   Collections let you store multiple values in one variable,
#   such as a group of numbers, words, or even objects.
# 
# Contents:
#   1. Lists — the Most Common Collection
#   2. Slicing Lists
#   3. Changing Items
#   4. Adding Items
#   5. Removing Items
#   6. Looping Through a List
#   7. Aliasing vs independent lists 
#   8. Useful List Functions
#     - min()
#     - max()
#     - sum()
#     - copy()
#   9. List Comprehensions
#   10. Nested Lists (Lists Inside Lists)
#   11. list() — the List Constructor



print("\n# -----------------------------")
print("# 1. Lists — the Most Common Collection")
print("# -----------------------------\n")

# A list is an ordered, changeable (mutable) collection.
fruits = ["apple", "banana", "cherry"]

# You can store any type of data inside:
mixed = [10, "hello", True, 3.14]

# ------------------------------------------------------------
# Accessing List Items (zero-indexed)
# ------------------------------------------------------------
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # cherry (last item). See more in negative_indices.py

# Trying to access a single index that is out of range raise an IndexError:
s = "abc"
try:
    print(s[10])
except Exception as e:
    print(f"Error, out of range: {type(e).__name__}")

print("\n# -----------------------------")
print("# 2. Slicing Lists")
print("# -----------------------------\n")

# Slicing returns a portion of the list. 

# list[start : stop : step]

# start →   index where the slice begins (inclusive)
# stop →    index where the slice ends (exclusive)
# step →    how many items to skip (optional). 
#           Step can be negative to reverse the slice. 
#           Step cannot be zero. Raising ValueError if you try.

print(fruits[0:2])   # ['apple', 'banana'] this makes slicing predictable -> 2 items
print(fruits[:2])    # ['apple', 'banana'] So the second number (2) is NOT included in the result.
print(fruits[1:])    # ['banana', 'cherry']
print(fruits[::-1])  # ['cherry', 'banana', 'apple'] (reverses the list)
# slicing with negative step skips every other from the end
print(list(range(5))[::-2])  # [4, 2, 0]

# Slicing with a negative step can be tricky. 
# The start index should be greater than the stop index for it to work.
s = "Python"
print("start > end in negative step: ", s[1:5:-1]) # empty string, because start index (1) is not greater than stop index (5) when stepping backwards.

# correct
s = "Python"
print("start < end in negative step: ", s[5:1:-1]) # 'nohty' 

# Slicing with a step of zero is not allowed and raises a ValueError.
lst = [1, 2, 3, 4, 5]
try:
    print(lst[1:3:0])
except Exception as e:
    print(f"Error, slice step cannot be zero: {type(e).__name__}") # Error: ValueError

# ------------------------------------------------------------
# Sliceing with a single index vs a range
# ------------------------------------------------------------

# Slicing with a range (like lst[0:1]) returns a list containing that item.
lst = [1, 2, 3, 4]
lst = lst[1:-1] 
print("Slicing with a range (1:-1) keeps the middle items:", lst)  # [2, 3]

# Slicing with a single index (like lst[0]) returns a single item 
lst = lst[-1] 
# lst is now an integer, not a list
print("The last item of the sliced list is:", lst, type(lst))  # 3     

# ------------------------------------------------------------
# Out-of-range slicing
# ------------------------------------------------------------

# out of range slicing does not raise an error, it just returns an empty list
s = "abc"
print(s[10:])  # slicing is forgiving with out-of-range indices


print("\n# -----------------------------")
print("# 3. Changing Items")
print("# -----------------------------\n")

fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']

# ------------------------------------------------------------
# Slice assignment — changing multiple items at once
# ------------------------------------------------------------

# replaces the selected range, not just a single item.
lst = [1, 2, 3, 4, 5]
lst[1:3] = [9, 8]
print("Changing multiple items at once - [9, 8] : ", lst)  # [1, 9, 8, 4, 5]

lst[1:4] = [11]  # this replaces the slice with a single item, so it removes the 9, 8, and 4 and puts 11 in their place
print("Changing multiple items at once - [11] : ",lst)  # [1, 11, 5]


print("\n# -----------------------------")
print("# 4. Adding Items")
print("# -----------------------------\n")

fruits.append("mango")     # adds to the end as a single item
fruits.insert(1, "pear")   # adds at position 1 as a single item even if the item is a list
fruits.extend(["kiwi", "grape"])  # adds each item from the iterable (like a list) to the end of the list
print(fruits)  # ['apple', 'pear', 'orange', 'cherry', 'mango', 'kiwi', 'grape']

print("\n# -----------------------------")
print("# 5. Removing Items")
print("# -----------------------------\n")

# # Remove by value:
fruits.remove("cherry")

# Or remove by index:
fruits.pop(0)   # removes first item
fruits.pop()    # remove last item

# Or delete by index with del:
del fruits[0]
# del fruits  # removes the entire list

# Delete a slice (remove multiple items at once):
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
del fruits[1:3]
print(fruits)  # ['apple', 'date', 'elderberry']


print("\n# -----------------------------")
print("# 6. Looping Through a List")
print("# -----------------------------\n")

for fruit in fruits:
    print(f"I like {fruit}")

# Loop with index:
for index, fruit in enumerate(fruits):
    print(index, fruit)

# enumerate() gives both index and value during iteration.

# ------------------------------------------------------------
# Getting List Length
# ------------------------------------------------------------
print(len(fruits))  # number of elements

# ------------------------------------------------------------
# Checking Membership
# ------------------------------------------------------------
print("apple" in fruits)     # True / False
print("kiwi" not in fruits)  # True / False

print("\n# -----------------------------")
print("# 7. Aliasing vs independent lists")
print("# -----------------------------\n")

# Assigning one list variable to another does NOT copy; both names point to same object.
x = [1, 2, 3]
y = x
y.append(4)
print("x after y.append:", x)  # [1, 2, 3, 4] → x and y reference the same list
print("y after y.append:", y)  # [1, 2, 3, 4]   

# Rebinding creates a new list object, leaving aliases untouched.
x = [1, 2, 3]
y = x
x = x + [4]  # new list produced; x now points to a different object
# it is equivalent to 
x = [1, 2, 3] + [4] # which creates a new list [1, 2, 3, 4] and assigns it to x
print("y stays referencing the original list:", y)  # [1, 2, 3]
print("x now points to a new list:", x)             # [1, 2, 3, 4]

# In-place operators mutate the existing list, so aliases see the change.
x = [1, 2, 3]
y = x
x += [4]  # extends the original object instead of rebinding
# it is equivalent to
x.extend([4]) # which modifies the original list that both x and y reference
print("y also sees the appended value due to shared reference:", y)     # [1, 2, 3, 4]
print("x references the same list object as y:", x is y)                # True

# NOTE: For numbers, x = x + 1 and x += 1 are equivalent because ints are immutable.
# With lists, x += [value] performs in-place modification (like list.extend),
# and x = x + [value] builds a brand-new list, which is why aliases behave differently.


print("\n# -----------------------------")
print("# 8. Useful List Functions")
print("# -----------------------------\n")

numbers = [4, 1, 8, 2, 9]
print(max(numbers))  # 9
print(min(numbers))  # 1
print(sum(numbers))  # 24

# ------------------------------------------------------------
# Copying Lists (same goal as slicing a[:])
# ------------------------------------------------------------
# Two common shallow-copy options:
a = [1, 2, 3]
b = a[:]  # slicing creates a new list object with the same items (shallow copy)
b.append(4)
print("a stays the same, b gets the new item:", a, b)   
# a: [1, 2, 3], 
# b: [1, 2, 3, 4]

nums_copy = numbers.copy()
print(nums_copy)    # [9, 8, 4, 2, 1]

# --- SHALLOW COPY (The "Slice" Trap) ---
# A slice [:] or .copy() creates a NEW container, but NESTED objects remain shared!

original_matrix = [[10, 20], [30, 40]]
cloned_matrix = original_matrix[:] # Shallow copy

# Scenario A: Changing a top-level element
cloned_matrix.append([50, 60]) 
# original_matrix is UNCHANGED. They are different list containers.
print("Original matrix after appending to clone:", original_matrix)  # [[10, 20], [30, 40]]
print("Cloned matrix after appending:", cloned_matrix)              # [[10, 20], [30, 40], [50, 60]]

# Scenario B: Changing a nested element (The Trap)
cloned_matrix[0][0] = 999 
# Both original_matrix[0][0] and cloned_matrix[0][0] are now 999!
# Because the internal list [10, 20] is the SAME object in memory for both.
print("Original matrix after modifying nested item:", original_matrix)  # [[999, 20], [30, 40]]
print("Cloned matrix after modifying nested item:", cloned_matrix)      # [[999, 20], [30, 40], [50, 60]]

# another example of the slice trap with a single nested list:
list_a = [1, [2, 3]]
list_b = list_a[:]

list_b.append(4)    # this changes only list_b, because it modifies the top-level list by adding a new item (4) which is a different object in list_b
list_b[0] = 7       # this changes only list_b, because it modifies the top-level item (the integer 1) which is a different object in list_b
list_b[1][0] = 77   # this changes both list_a and list_b, because it modifies the nested list [2, 3] which is the same object in both lists
print("list_a after modifications to list_b:", list_a)  # [1, [77, 3]] → the first item (1) is unchanged because it is a different object in list_a, but the nested list is modified in both because it is shared
print("list_b after modifications:", list_b)            # [7, [77, 3], 4] → the first item is changed to 99, the nested list is modified to [77, 3], and 4 is added at the end

print("\n# -----------------------------")
print("# 9. List Comprehensions")
print("# -----------------------------\n")

# List comprehensions provide a concise way to create lists.
# Create a list of squares
squares = [n * n for n in numbers]
print(squares)      # [81, 64, 16, 4, 1]

# Filter even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers) # [8, 2]

# List repetition duplicates the list content N times.
print([1, 2] * 2)   # [1, 2, 1, 2]
print([1, 2] * 4)   # [1, 2, 1, 2, 1, 2, 1, 2]

# what might confuse beginners is that len() counts total items:
print(len([0] * 3 + [1] * 2))  # 5
print([0] * 3 + [1] * 2)  # [0, 0, 0, 1, 1]

# Be cautious with nested mutable objects:
triplicated = [[]] * 3
print(triplicated, "len:", len(triplicated)) # [[], [], []] len: 3
# All three references point to the same inner list object.
# for example, modifying one modifies all:
triplicated[0].append("wow")
print(triplicated, "len:", len(triplicated)) # [['wow'], ['wow'], ['wow']]

# To create independent inner lists, use a list comprehension:
independent = [[] for _ in range(3)]
print(independent, "len:", len(independent)) # [[], [], []] len: 3
# Now modifying one does not affect the others:
independent[0].append("wow")
print(independent, "len:", len(independent)) # [['wow'], [], []]    

triplicated[0].append("now")
print("Appending via one reference touches all:", triplicated) 
# [['wow', 'now'], ['wow', 'now'], ['wow', 'now']]
# why append does not replace 'wow' with 'now'? because append adds to the existing list
# to replace, you would do triplicated[0] = ['now']


print("\n# -----------------------------")
print("# 10. nested lists (lists inside lists)")
print("# -----------------------------\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6

# Looping through nested lists
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()  # new line after each row

print("\n# -----------------------------")
print("# 11. list()")
print("# -----------------------------\n")

# list() is a constructor used to create a new list object. 
# While often grouped with methods, it is technically a built-in class 
# that builds a list from other data types.

# Primary Uses
# Empty List: 
#  - Calling list() with no arguments returns an empty list [].
empty_list = list()

# Type Conversion: 
#  - It converts any iterable (like a string, tuple, set, or dictionary) into a list.
string_list = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# Shallow Copy: 
#  - Calling list(another_list) creates a new list object containing references to the original items.
# These references mean that if the original list contains mutable objects (like other lists), 
# changes to those objects will be reflected in both lists, but adding or removing items from one list will not affect the other. 
original = [1, 2, 3]
shallow_copy = list(original)
shallow_copy.append(4)
print("original:", original)        # [1, 2, 3]
print("shallow_copy:", shallow_copy) # [1, 2, 3, 4]

shallow_copy[0] = 0 # this modifies the shallow copy, but does not affect the original list because integers are immutable
print("original after modifying shallow_copy:", original)        # [1, 2, 3]
print("shallow_copy after modification:", shallow_copy)          # [0, 2, 3, 4]

# Performance Note
# For creating an empty list, using square brackets [] is significantly faster (roughly 3x)
# than calling list() because the literal [] is a single bytecode instruction, while list()
# requires a function call and name lookup. 
# Use list() specifically for conversion or when you need a factory function.



