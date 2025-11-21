# ==============================================
# Before Pattern: Flyweight
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how many similar objects (trees in a forest) were created
#   BEFORE applying the Flyweight pattern. Each Tree keeps its own heavy
#   data (like texture information), which wastes memory when thousands of
#   nearly identical trees are used.
# ==============================================


# -----------------------------
# Tree class (no shared data)
# -----------------------------
class Tree:
    def __init__(self, x, y, color, texture_data):
        # Position (lightweight, unique per tree)
        self.x = x
        self.y = y
        # Appearance (heavy, but duplicated for every tree)
        self.color = color
        self.texture_data = texture_data  # imagine a large image or sprite

    def draw(self):
        print(
            f"Drawing tree at ({self.x}, {self.y}) "
            f"with color={self.color} and texture={self.texture_data}"
        )


# -----------------------------
# Forest (Before Flyweight)
# -----------------------------
# NOTE:
#   Each Tree stores its own copy of texture_data, even if many trees
#   look exactly the same. With thousands of trees, memory usage grows
#   quickly and wastes resources.
# -----------------------------

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, color, texture_data):
        tree = Tree(x, y, color, texture_data)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Flyweight Pattern Example ---\n")

    forest = Forest()

    # Plant several trees that share the same appearance
    heavy_texture = "[BIG_TREE_TEXTURE_DATA]"  # imagine huge image data

    forest.plant_tree(1, 1, "green", heavy_texture)
    forest.plant_tree(2, 3, "green", heavy_texture)
    forest.plant_tree(5, 8, "green", heavy_texture)

    forest.draw()

    print(
        "\nIn a real game, there might be thousands of similar trees.\n"
        "Each Tree here stores its OWN copy of texture_data, even if it is\n"
        "identical. This leads to duplicated heavy data and high memory use.\n"
        "The Flyweight pattern solves this by sharing common state between objects."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Flyweight Pattern Example ---
# Drawing tree at (1, 1) with color=green and texture=[BIG_TREE_TEXTURE_DATA]
# Drawing tree at (2, 3) with color=green and texture=[BIG_TREE_TEXTURE_DATA]
# Drawing tree at (5, 8) with color=green and texture=[BIG_TREE_TEXTURE_DATA]
#
# In a real game, there might be thousands of similar trees.
# Each Tree here stores its OWN copy of texture_data, even if it is
# identical. This leads to duplicated heavy data and high memory use.
# The Flyweight pattern solves this by sharing common state between objects.
#
# ==============================================
# History
# ==============================================
# The Flyweight pattern was described in the GoF book (1994) as a way to
# reduce memory use when many fine-grained objects share the same data.
# It became popular in text rendering, GUI widgets, and games, where
# characters, icons, or trees can share intrinsic state instead of storing
# it separately in every instance.
# ==============================================
