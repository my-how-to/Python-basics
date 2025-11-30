# ==============================================
# Pattern Name: Memento
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Memento pattern captures and restores an object's internal state
#   without exposing implementation details. This example uses **car
#   settings presets** (seat, mirrors, AC) that a driver can save and
#   restore.
#
# Classifier:
#   - Category: Behavioral
#   - Purpose: Save and restore object state without breaking encapsulation.
#   - Key idea: Originator creates snapshots; Caretaker stores them.
#   - Common use: Undo/redo systems, checkpoints, configuration backups.
#
# What Makes It Unique:
#   Memento allows time-travel-like behavior while keeping internal
#   variables private. Only the originator can read or write mementos.
# ==============================================


# -----------------------------
# Memento (Snapshot of car settings)
# -----------------------------
class CarSettingsMemento:
    # Stores a snapshot of car settings.
    # Only CarSettings (Originator) should know how to use it.
    def __init__(self, seat, mirrors, ac):
        self._seat = seat
        self._mirrors = mirrors
        self._ac = ac


# -----------------------------
# Originator (Car Settings)
# -----------------------------
class CarSettings:
    # Holds the internal state and knows how to save/restore it.
    def __init__(self):
        self.seat = 0
        self.mirrors = "neutral"
        self.ac = 20

    def set_settings(self, seat, mirrors, ac):
        self.seat = seat
        self.mirrors = mirrors
        self.ac = ac
        print(f"Settings applied → Seat:{seat}, Mirrors:{mirrors}, AC:{ac}")

    def save(self):
        # Create a snapshot of the current car settings.
        print("Saving current settings...")
        return CarSettingsMemento(self.seat, self.mirrors, self.ac)

    def restore(self, memento):
        self.seat = memento._seat
        self.mirrors = memento._mirrors
        self.ac = memento._ac
        print(f"Restored → Seat:{self.seat}, Mirrors:{self.mirrors}, AC:{self.ac}")
        
        # NOTE:
        #   If CarSettings receives a new internal field (e.g., steering),
        #   ONLY this Originator class and its Memento class require updates.
        #   External code (PresetManager, UI, load/save operations) remains unchanged.
        #   This is the key advantage of the Memento pattern — encapsulation.


# -----------------------------
# Caretaker (Stores saved presets)
# -----------------------------
class PresetManager:
    # Stores mementos but never modifies internal data.
    def __init__(self):
        self._presets = {}

    def save_preset(self, name, memento):
        self._presets[name] = memento
        print(f"Preset '{name}' saved.")

    def load_preset(self, name):
        return self._presets.get(name)


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Memento Pattern Example (Car Settings) ---\n")

    car = CarSettings()
    presets = PresetManager()

    print("# -----------------------------")
    print("# CONFIGURATION TIME (saving presets)")
    print("# -----------------------------\n")

    # Comfort mode
    car.set_settings(70, "wide", 22)
    presets.save_preset("comfort", car.save())

    print()  # spacing

    # Sport mode
    car.set_settings(40, "narrow", 18)
    presets.save_preset("sport", car.save())

    print("\n# -----------------------------")
    print("# REAL-WORLD USAGE (restoring presets)")
    print("# -----------------------------\n")

    # Restore comfort
    print(">>> Restoring 'comfort' preset...")
    comfort_memento = presets.load_preset("comfort")
    car.restore(comfort_memento)

    print()  # spacing

    # Restore sport
    print(">>> Restoring 'sport' preset...")
    sport_memento = presets.load_preset("sport")
    car.restore(sport_memento)

    print("\n# -----------------------------")
    print("# ADVANTAGE DEMO (Memento survives internal changes)")
    print("# -----------------------------\n")

    print(">>> Now the car receives a NEW internal field: 'steering' (simulating a software update)")
    car.steering = 5
    print(f"Applied new steering value: {car.steering}")

    print("\nApplying a new setting that includes the new 'steering' field...")
    car.set_settings(55, "wide", 21)
    car.steering = 9
    print(f"Updated steering value: {car.steering}")

    print("\nSaving a new preset AFTER the internal change (Memento ignores unrelated fields)...")
    new_preset = car.save()

    print("\n>>> Restoring old preset 'comfort' (notice internal integrity is preserved)")
    car.restore(comfort_memento)

    print(f"Current steering value (unchanged because Memento preserves encapsulation): {car.steering}")


# -----------------------------
# Example Output
# -----------------------------
# --- Memento Pattern Example (Car Settings) ---
#
# -----------------------------
# CONFIGURATION TIME (saving presets)
# -----------------------------
# Settings applied → Seat:70, Mirrors:wide, AC:22
# Saving current settings...
# Preset 'comfort' saved.
#
# Settings applied → Seat:40, Mirrors:narrow, AC:18
# Saving current settings...
# Preset 'sport' saved.
#
# -----------------------------
# REAL-WORLD USAGE (restoring presets)
# -----------------------------
# >>> Restoring 'comfort' preset...
# Restored → Seat:70, Mirrors:wide, AC:22
#
# >>> Restoring 'sport' preset...
# Restored → Seat:40, Mirrors:narrow, AC:18
#
# -----------------------------
# ADVANTAGE DEMO (Memento survives internal changes)
# -----------------------------
# >>> Now the car receives a NEW internal field: 'steering' (simulating a software update)
# Applied new steering value: 5
#
# Applying a new setting that includes the new 'steering' field...
# Settings applied → Seat:55, Mirrors:wide, AC:21
# Updated steering value: 9
#
# Saving a new preset AFTER the internal change (Memento ignores unrelated fields)...
# Saving current settings...
#
# >>> Restoring old preset 'comfort' (notice internal integrity is preserved)
# Restored → Seat:70, Mirrors:wide, AC:22
# Current steering value (unchanged because Memento preserves encapsulation): 9
#
#
# ==============================================
# History
# ==============================================
# The Memento pattern was formalized in 1994 in the "Design Patterns"
# book by the Gang of Four. It emerged from the need for undo/redo
# mechanisms in editors, games, drawing tools, and configuration systems.
# By encapsulating snapshots of internal state, programs gained the ability
# to roll back changes without exposing sensitive internal data.
# ==============================================
