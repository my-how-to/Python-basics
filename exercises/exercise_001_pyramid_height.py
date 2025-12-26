# ============================================================
#                EXERCISE 001 — PYRAMID HEIGHT
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise (PCEP course task):
#   Builders are stacking a pyramid, one layer at a time.
#   The first layer needs 1 block, the next needs 2, then 3, and so on.
#
#   Read how many blocks they have in total.
#   Build as many full layers as possible.
#   If the next layer can't be finished, stop and print the height
#   (the number of complete layers).
#
# Solution:
#   Repeatedly subtract the blocks required for each layer, starting
#   from 1 and increasing by 1 each time. Count how many full layers
#   can be completed.
# ============================================================


# ------------------------------------------------------------
# WHILE-LOOP SOLUTION
# ------------------------------------------------------------
# This version is direct because we don't know how many layers
# will fit. We keep subtracting until the next layer can't be built.

blocks = int(input("Enter the number of blocks (while loop): "))

height = 0
current_layer_blocks = 1

while blocks >= current_layer_blocks:
    blocks -= current_layer_blocks
    current_layer_blocks += 1  # manual step to grow the next layer size
    height += 1

print("Pyramid height (while loop):", height)

# ------------------------------------------------------------
# FOR-LOOP VARIANT
# ------------------------------------------------------------
# The for-loop version still works, but needs a break
# once blocks run out, and it uses range() to advance layer size.

blocks = int(input("Enter the number of blocks (for loop): "))

height = 0

for current_layer_blocks in range(1, blocks + 1): 
    if blocks < current_layer_blocks:
        break
    blocks -= current_layer_blocks
    height += 1

print("Pyramid height (for loop):", height)
