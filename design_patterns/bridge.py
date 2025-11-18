# ==============================================
# Pattern Name: Bridge
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Bridge pattern separates a high-level abstraction (Shape)
#   from its low-level implementation (DrawingAPI). This allows both
#   sides to vary independently, preventing subclass explosion when
#   adding new shapes or new drawing systems.
#
# What Makes It Unique:
#   Bridge decouples *what* is drawn (Shape) from *how* it is drawn
#   (DrawingAPI). Both hierarchies grow independently without affecting
#   each other.
# ==============================================


# -----------------------------
# Implementor Interface
# -----------------------------
# This interface defines HOW shapes are drawn.
# The abstraction (Shape) will delegate drawing work here.
# Adding a new drawing system (SVG, OpenGL, PDF, etc.)
# means creating another class that implements these methods.
# -----------------------------
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        raise NotImplementedError

    def draw_square(self, x, y, side):
        raise NotImplementedError


# -----------------------------
# Concrete Implementors
# -----------------------------
# These classes provide the actual drawing operations.
# Shapes do not care about HOW drawing works — they only
# call the drawing API through this interface.
# This lets us plug in new drawing engines without touching shapes.
# -----------------------------
class VectorDrawingAPI(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Vector: Drawing Circle at ({x}, {y}) with radius {radius}")

    def draw_square(self, x, y, side):
        print(f"Vector: Drawing Square at ({x}, {y}) with side {side}")


class RasterDrawingAPI(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Raster: Drawing Circle at ({x}, {y}) with radius {radius}")

    def draw_square(self, x, y, side):
        print(f"Raster: Drawing Square at ({x}, {y}) with side {side}")


# -----------------------------
# Abstraction
# -----------------------------
# Shape represents the high-level concept: circle, square, etc.
# It stores a reference to a DrawingAPI but does NOT implement drawing.
# This is the core decoupling: shapes know WHAT they are,
# drawing APIs know HOW to draw them.
# -----------------------------
class Shape:
    def __init__(self, drawing_api: DrawingAPI):
        self.drawing_api = drawing_api

    def draw(self):
        raise NotImplementedError


# -----------------------------
# Refined Abstractions
# -----------------------------
# Circle is a refined abstraction.
# It defines WHAT a circle is, but delegates HOW it is drawn
# to the DrawingAPI provided.
class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print("Drawing Circle (Abstraction → Implementor)")
        self.drawing_api.draw_circle(self.x, self.y, self.radius)


# Square is another refined abstraction.
# Again — it describes the shape, not the drawing mechanics.
class Square(Shape):
    def __init__(self, x, y, side, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.side = side

    def draw(self):
        print("Drawing Square (Abstraction → Implementor)")
        self.drawing_api.draw_square(self.x, self.y, self.side)


# -----------------------------
# Example usage
# -----------------------------
# Here we combine:
#   - the abstraction (Shape subclasses)
#   - the implementation (DrawingAPI subclasses)
# The same Circle can be drawn with different APIs without modifying
# the Circle class — demonstrating complete decoupling.
# -----------------------------
if __name__ == "__main__":
    print("--- Bridge Pattern Example ---\n")

    vector_api = VectorDrawingAPI()
    raster_api = RasterDrawingAPI()

    shape1 = Circle(10, 20, 5, vector_api)
    shape2 = Square(5, 5, 3, raster_api)

    shape1.draw()
    shape2.draw()


# -----------------------------
# Example Output
# -----------------------------
# --- Bridge Pattern Example ---
# Drawing Circle (Abstraction → Implementor)
# Vector: Drawing Circle at (10, 20) with radius 5
# Drawing Square (Abstraction → Implementor)
# Raster: Drawing Square at (5, 5) with side 3
#
#
# ==============================================
# History
# ==============================================
# The Bridge pattern was formalized in the GoF (1994) as a solution to
# avoid the combinational explosion of subclasses when two dimensions
# of change exist (e.g., shapes and drawing styles). By separating the
# abstraction and implementation hierarchies, both can evolve without
# affecting each other.
# ==============================================
