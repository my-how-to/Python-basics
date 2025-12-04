# ==============================================
# BEFORE — Visitor Pattern
# Theme: Zoo Animals Processed Without Visitor (Multiple Operations)
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Before the Visitor pattern, adding new operations for existing
#   objects (animals) required modifying every class or writing large
#   if/elif blocks. This violates the Open–Closed Principle.
#
#   In this BEFORE example, we demonstrate a zoo where different
#   operations must be performed on multiple animals: feeding,
#   medical checkups, and cleaning. The logic is messy, duplicated,
#   and fragile.
# ==============================================


# -----------------------------
# BEFORE: Animals represented as simple objects
# -----------------------------
class Lion:
    def __init__(self):
        self.name = "Lion"

class Elephant:
    def __init__(self):
        self.name = "Elephant"

class Monkey:
    def __init__(self):
        self.name = "Monkey"


# -----------------------------
# BEFORE: Functions performing operations with if/elif logic
# -----------------------------
def feed(animal):
    print(f"Feeding: {animal.name}")

    if isinstance(animal, Lion):
        print("Giving meat...")

    elif isinstance(animal, Elephant):
        print("Giving vegetables and fruit...")

    elif isinstance(animal, Monkey):
        print("Giving bananas...")

    print()


def medical_check(animal):
    print(f"Medical check for: {animal.name}")

    if isinstance(animal, Lion):
        print("Checking claws and teeth...")

    elif isinstance(animal, Elephant):
        print("Checking trunk and weight...")

    elif isinstance(animal, Monkey):
        print("Checking agility and fur...")

    print()


def clean_enclosure(animal):
    print(f"Cleaning enclosure for: {animal.name}")

    if isinstance(animal, Lion):
        print("Removing bones and cleaning den...")

    elif isinstance(animal, Elephant):
        print("Removing branches and spraying water...")

    elif isinstance(animal, Monkey):
        print("Cleaning climbing structures...")

    print()


# -----------------------------
# Example Usage (Before Visitor)
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE Visitor Example (Zoo Animals) ---\n")

    animals = [Lion(), Elephant(), Monkey()]

    print("# -----------------------------")
    print("# BASIC OPERATIONS")
    print("# -----------------------------\n")

    for animal in animals:
        feed(animal)
        medical_check(animal)
        clean_enclosure(animal)

    print("# -----------------------------")
    print("# DISADVANTAGE DEMO (Adding New Operation Breaks Everything)")
    print("# -----------------------------\n")

    print("Adding new operation: 'record_daily_activity'\n")

    def record_daily_activity(animal):
        print(f"Recording activity for: {animal.name}")

        if isinstance(animal, Lion):
            print("Lion activity: prowling and resting.")
        elif isinstance(animal, Elephant):
            print("Elephant activity: grazing and bathing.")
        elif isinstance(animal, Monkey):
            print("Monkey activity: climbing and playing.")
        print()

    for animal in animals:
        record_daily_activity(animal)

    print("# NOTE: Each new animal OR new operation requires editing code everywhere.")


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE Visitor Example (Zoo Animals) ---
#
# Feeding: Lion
# Giving meat...
#
# Feeding: Elephant
# Giving vegetables and fruit...
#
# Feeding: Monkey
# Giving bananas...
#
# Medical check for: Lion
# Checking claws and teeth...
#
# Medical check for: Elephant
# Checking trunk and weight...
#
# Medical check for: Monkey
# Checking agility and fur...
#
# Cleaning enclosure for: Lion
# Removing bones and cleaning den...
#
# Cleaning enclosure for: Elephant
# Removing branches and spraying water...
#
# Cleaning enclosure for: Monkey
# Cleaning climbing structures...
#
# -----------------------------
# DISADVANTAGE DEMO (Adding New Operation Breaks Everything)
# -----------------------------
# Adding new operation: 'record_daily_activity'
# Recording activity for: Lion
# Lion activity: prowling and resting.
#
# Recording activity for: Elephant
# Elephant activity: grazing and bathing.
#
# Recording activity for: Monkey
# Monkey activity: climbing and playing.
#
# NOTE: Every new operation requires repeating large if/elif structures.
#       Every new ANIMAL requires modifying ALL existing operations.
#       This is exactly what the Visitor Pattern solves.
#
#
# ==============================================
# History
# ==============================================
# Before the Visitor pattern, developers scattered logic across many
# functions or methods using isinstance checks or if/elif chains.
# Systems with many object types (like AST nodes, UI elements, or data
# structures) became extremely hard to extend.
#
# The Visitor pattern centralized operations into separate *visitor*
# classes, allowing new behaviors to be added without modifying the
# existing object hierarchy.
# ==============================================
