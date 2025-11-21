# ==============================================
# Pattern Name: Flyweight
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Flyweight pattern reduces memory usage by sharing common,
#   immutable data (intrinsic state) between many small objects.
#   In this example, Tree position is unique per tree, but the
#   appearance (color + texture) is shared as a Flyweight.
#
# What Makes It Unique:
#   Flyweight separates intrinsic (shared) and extrinsic (unique) data.
#   This allows thousands of lightweight objects to reuse the same
#   heavy data instead of duplicating it.
# ==============================================


# -----------------------------
# Flyweight: TreeType
# -----------------------------
# Stores shared, reusable data about trees (appearance).
# -----------------------------
class TreeType:
    def __init__(self, color, texture_data):
        self.color = color
        self.texture_data = texture_data  # heavy shared data

    def draw(self, x, y):
        print(
            f"Drawing tree at ({x}, {y}) with color={self.color} "
            f"and texture={self.texture_data} (shared)"
        )


# -----------------------------
# Flyweight Factory
# -----------------------------
# Ensures TreeTypes are reused instead of recreated.
# -----------------------------
class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, color, texture_data):
        key = (color, texture_data)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(color, texture_data)
            print(f"Creating NEW TreeType for color={color}")
        else:
            print(f"Reusing EXISTING TreeType for color={color}")
        return cls._tree_types[key]


# -----------------------------
# Lightweight Object: Tree
# -----------------------------
# Stores only extrinsic (unique) data like position.
# Appearance is stored in the shared TreeType.
# -----------------------------
class Tree:
    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type  # shared

    def draw(self):
        self.tree_type.draw(self.x, self.y)


# -----------------------------
# Forest using Flyweight
# -----------------------------
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, color, texture_data):
        tree_type = TreeFactory.get_tree_type(color, texture_data)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Flyweight Pattern Example ---\n")

    forest = Forest()
    heavy_texture = "[BIG_TREE_TEXTURE_DATA]"

    # Plant several trees that share the same appearance
    forest.plant_tree(1, 1, "green", heavy_texture)
    forest.plant_tree(2, 3, "green", heavy_texture)
    forest.plant_tree(5, 8, "green", heavy_texture)

    forest.draw()


# -----------------------------
# Example Output
# -----------------------------
# --- Flyweight Pattern Example ---
# Creating NEW TreeType for color=green
# Reusing EXISTING TreeType for color=green
# Reusing EXISTING TreeType for color=green
# Drawing tree at (1, 1) with color=green and texture=[BIG_TREE_TEXTURE_DATA] (shared)
# Drawing tree at (2, 3) with color=green and texture=[BIG_TREE_TEXTURE_DATA] (shared)
# Drawing tree at (5, 8) with color=green and texture=[BIG_TREE_TEXTURE_DATA] (shared)
#
# ==============================================
# History
# ==============================================
# The Flyweight pattern (GoF 1994) was introduced to solve memory
# problems caused by large numbers of similar objects. It is commonly
# used in text rendering, GUI component libraries, document editors,
# and games where many objects share the same appearance.
# ==============================================
