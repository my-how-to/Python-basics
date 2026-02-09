# ============================================================
#            LESSON 11.1 - COMPREHENSIONS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains comprehensions in Python: list,
#   dictionary, set comprehensions, nested comprehensions,
#   and generator expressions.  
#
#  Comprehensions let you build collections in a single, expressive line.
#
# Contents:
#   1. List Comprehensions
#   2. Dictionary Comprehensions
#   3. Set Comprehensions
#   4. Nested Comprehensions
#   5. Extra Notes
# 
# ============================================================
# 1) List Comprehensions
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Classic loop
squares_loop = []
for n in numbers:
    squares_loop.append(n ** 2)
print(squares_loop)

# List comprehension (shorter + expressive)
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# With condition
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16]

#This list returns all numbers from 0 to 5 that are NOT divisible by 3.
print([i for i in range(6) if i % 3])  # [1, 2, 4, 5]

# ============================================================
# 2) Dictionary Comprehensions
# ============================================================

numbers_small = [1, 2, 3, 4]
squares_dict = {n: n ** 2 for n in numbers_small}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16}

# ============================================================
# 3) Set Comprehensions
# ============================================================

unique_lengths = {len(word) for word in ["apple", "banana", "pear"]}
print(unique_lengths)  # {4, 5, 6}

# ============================================================
# 4) Nested Comprehensions
# ============================================================

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# Equivalent regular loop
pairs_loop = []
for x in [1, 2]:
    for y in [3, 4]:
        pairs_loop.append((x, y))
print(pairs_loop)

# ============================================================
# 5) Extra Notes
# ============================================================

# Generator expressions look like list comprehensions, but use parentheses:
gen = (n ** 2 for n in numbers)
print("next(gen): ", next(gen))  # lazily produces values on demand
# next(gen)  # call repeatedly to get next values

# Tuple-style parentheses vs list brackets for visual contrast
list_version = [n ** 2 for n in numbers]
generator_version = (n ** 2 for n in numbers)
print("List version: ", list_version)           # materialized list
print("Generator version: ", generator_version)      # generator object (use next()/iteration)

# Keep comprehensions readable. If logic gets complex or deeply nested,
# fall back to regular loops for clarity.
