# ==============================================
# Before Pattern: Abstract Factory
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how GUI widgets (Button, Checkbox, Icon) were created
#   manually before the Abstract Factory pattern. Developers used
#   long chains of if/else statements to match widget families.
#   Adding new themes or new widget types caused code duplication
#   and required modifying many parts of the program.
# ==============================================


# -----------------------------
# GUI Widgets (Manual Creation)
# -----------------------------
class DarkButton:
    def draw(self):
        print("Drawing Dark Button")


class LightButton:
    def draw(self):
        print("Drawing Light Button")


class DarkCheckbox:
    def draw(self):
        print("Drawing Dark Checkbox")


class LightCheckbox:
    def draw(self):
        print("Drawing Light Checkbox")


class DarkIcon:
    def draw(self):
        print("Drawing Dark Icon")


class LightIcon:
    def draw(self):
        print("Drawing Light Icon")


# -----------------------------
# Widget Builder (Before Pattern)
# -----------------------------
# NOTE:
# When adding a new widget type (e.g., Icon or Slider), developers had to
# update EVERY if/else block in EVERY place where widgets were created.
# This caused inconsistency and bugs.
# -----------------------------

def create_widgets(theme):
    """
    Manually create matching button + checkbox + icon using if/else logic.
    Before Abstract Factory, this logic appeared in many modules.
    """

    if theme == "dark":
        button = DarkButton()
        checkbox = DarkCheckbox()
        icon = DarkIcon()

    elif theme == "light":
        button = LightButton()
        checkbox = LightCheckbox()
        icon = LightIcon()

    else:
        raise ValueError("Unknown theme")

    return button, checkbox, icon


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Abstract Factory Example ---\n")

    theme = "dark"
    button, checkbox, icon = create_widgets(theme)

    print(f"Selected theme: {theme}")
    button.draw()
    checkbox.draw()
    icon.draw()

    print(
        "\nAdding a new widget (like Slider) requires updating all if/else blocks\n"
        "across the entire codebase."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Abstract Factory Example ---
#
# Selected theme: dark
# Drawing Dark Button
# Drawing Dark Checkbox
# Drawing Dark Icon
#
# Adding a new widget (like Slider) requires updating all if/else blocks
# across the entire codebase.
#
#
# ==============================================
# History
# ==============================================
# Before the Abstract Factory pattern (GoF, 1994), GUI widget creation relied
# heavily on repetitive if/else logic. Adding a new theme or widget type
# required modifying many modules, leading to inconsistent behavior and bugs.
# Abstract Factory solved this by centralizing creation of entire product
# families behind a single factory interface.
# ==============================================
