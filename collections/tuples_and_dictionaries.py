# ============================================================
#   LESSON — TUPLES AND DICTIONARIES TOGETHER (COLLECTIONS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson shows how tuples and dictionaries work together:
#   tuple keys for composite lookup, tuple values for grouped data,
#   and unpacking key/value pairs with items().
#
# Contents:
#   1. Tuples as Dictionary Keys
#   2. Tuples as Dictionary Values
#   3. Unpacking items()
#
print("\n# -----------------------------")
print("# 1. Tuples as Dictionary Keys")
print("# -----------------------------\n")

# Tuples are immutable, so they can be used as dictionary keys.
locations = {
    (0, 0): "origin",
    (10, 5): "checkpoint",
    (-3, 2): "marker",
}

print(locations[(0, 0)])   # origin
print(locations[(10, 5)])  # checkpoint

print("\n# -----------------------------")
print("# 2. Tuples as Dictionary Values")
print("# -----------------------------\n")

# Use tuple values to group related data under one key.
employees = {
    "Alex": ("QA", 5),
    "Maria": ("Dev", 3),
    "Lee": ("PM", 7),
}

role, years = employees["Maria"]
print(role, years)  # Dev 3

print("\n# -----------------------------")
print("# 3. Unpacking items()")
print("# -----------------------------\n")

# items() returns (key, value) tuples that you can unpack directly.
for name, (role, years) in employees.items():
    print(name, "→", role, years) 

# Output:
# Alex → QA 5
# Maria → Dev 3
# Lee → PM 7
