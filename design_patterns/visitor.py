# ==============================================
# Pattern Name: Visitor
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   The Visitor pattern lets you add new operations to existing classes
#   (animals) without modifying those classes. Instead, operations are
#   placed inside separate Visitor objects.
#
#   In this example, a zoo contains animals (Lion, Elephant, Monkey).
#   Different visitors (Feeder, Vet, Cleaner) perform operations on them.
#   Adding a new visitor or new operation does NOT require modifying the
#   existing animal classes.
#
# What Makes It Unique:
#   - New operations can be added by creating new Visitor classes.
#   - Animal classes remain unchanged.
#   - Eliminates large if/elif isinstance checks.
# ==============================================


# -----------------------------
# Visitor Interface
# -----------------------------
class AnimalVisitor:
    def visit_lion(self, lion):
        raise NotImplementedError

    def visit_elephant(self, elephant):
        raise NotImplementedError

    def visit_monkey(self, monkey):
        raise NotImplementedError


# -----------------------------
# Animal Classes (Elements)
# -----------------------------
class Lion:
    def accept(self, visitor: AnimalVisitor):
        visitor.visit_lion(self)

class Elephant:
    def accept(self, visitor: AnimalVisitor):
        visitor.visit_elephant(self)

class Monkey:
    def accept(self, visitor: AnimalVisitor):
        visitor.visit_monkey(self)


# -----------------------------
# Concrete Visitors (Operations)
# -----------------------------
class Feeder(AnimalVisitor):
    def visit_lion(self, lion):
        print("Feeding lion: meat.")

    def visit_elephant(self, elephant):
        print("Feeding elephant: vegetables and fruit.")

    def visit_monkey(self, monkey):
        print("Feeding monkey: bananas.")


class Vet(AnimalVisitor):
    def visit_lion(self, lion):
        print("Checking lion: claws and teeth.")

    def visit_elephant(self, elephant):
        print("Checking elephant: trunk and weight.")

    def visit_monkey(self, monkey):
        print("Checking monkey: agility and fur.")


class Cleaner(AnimalVisitor):
    def visit_lion(self, lion):
        print("Cleaning lion enclosure: removing bones.")

    def visit_elephant(self, elephant):
        print("Cleaning elephant area: removing branches.")

    def visit_monkey(self, monkey):
        print("Cleaning monkey zone: scrubbing climbing structures.")


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    print("--- Visitor Pattern Example (Zoo Animals) ---\n")

    animals = [Lion(), Elephant(), Monkey()]
    visitors = [Feeder(), Vet(), Cleaner()]

    print("# -----------------------------")
    print("# USING VISITOR PATTERN")
    print("# -----------------------------\n")

    for visitor in visitors:
        print(f"Applying visitor: {visitor.__class__.__name__}")
        for animal in animals:
            animal.accept(visitor)
        print()


# -----------------------------
# Example Output
# -----------------------------
# --- Visitor Pattern Example (Zoo Animals) ---
#
# -----------------------------
# USING VISITOR PATTERN
# -----------------------------
# Applying visitor: Feeder
# Feeding lion: meat.
# Feeding elephant: vegetables and fruit.
# Feeding monkey: bananas.
#
# Applying visitor: Vet
# Checking lion: claws and teeth.
# Checking elephant: trunk and weight.
# Checking monkey: agility and fur.
#
# Applying visitor: Cleaner
# Cleaning lion enclosure: removing bones.
# Cleaning elephant area: removing branches.
# Cleaning monkey zone: scrubbing climbing structures.
#
#
# ==============================================
# History
# ==============================================
# The Visitor pattern was designed for cases where many unrelated
# operations must be performed on objects in a stable hierarchy. Instead
# of modifying the classes every time a new operation is needed, Visitor
# allows operations to be defined externally. This is widely used in
# compilers, AST processing, document export systems, and hierarchical
# data traversal.
# ==============================================
