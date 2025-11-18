# ==============================================
# Before Pattern: Bridge
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how shapes and drawing methods were tightly coupled
#   BEFORE applying the Bridge pattern. Each combination of Shape × DrawingAPI
#   required its own class (e.g., VectorCircle, RasterCircle). As the number
#   of shapes and drawing styles grows, subclasses explode in number.
#   This leads to code duplication and is hard to maintain.
# ==============================================


# -----------------------------
# Shape × Drawing Combination Classes
# -----------------------------
# NOTE:
#   These classes mix BOTH the shape and the drawing method.
#   Adding a new shape OR a new drawing API requires many new classes.
# -----------------------------

class VectorCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle using VECTOR API at ({self.x}, {self.y}) with radius {self.radius}")


class RasterCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle using RASTER API at ({self.x}, {self.y}) with radius {self.radius}")


class VectorSquare:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def draw(self):
        print(f"Drawing Square using VECTOR API at ({self.x}, {self.y}) with side {self.side}")


class RasterSquare:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def draw(self):
        print(f"Drawing Square using RASTER API at ({self.x}, {self.y}) with side {self.side}")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Bridge Pattern Example ---\n")

    circle = VectorCircle(10, 20, 5)
    circle.draw()

    square = RasterSquare(5, 5, 3)
    square.draw()

    print(
        "\nAdding a new Shape (like Triangle) requires creating BOTH:\n"
        " - VectorTriangle\n"
        " - RasterTriangle\n\n"
        "Adding a new Drawing API (like SVG) requires creating:\n"
        " - SvgCircle, SvgSquare, SvgTriangle, ... for every shape.\n"
        "This leads to subclass explosion."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Bridge Pattern Example ---
# Drawing Circle using VECTOR API at (10, 20) with radius 5
# Drawing Square using RASTER API at (5, 5) with side 3
#
# Adding a new Shape (like Triangle) requires:
#  - VectorTriangle
#  - RasterTriangle
#
# Adding a new Drawing API (like SVG) requires:
#  - SvgCircle, SvgSquare, SvgTriangle, ...
# This leads to subclass explosion.
#
#
# ==============================================
# History
# ==============================================
# Before the Bridge pattern (GoF 1994), developers combined abstraction
# (shape) with implementation (rendering API) in the same class. This caused
# rapid subclass growth when either dimension expanded. The Bridge pattern
# solves this by separating the two hierarchies.
# ==============================================
