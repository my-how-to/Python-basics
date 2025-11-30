# ==============================================
# BEFORE — Memento Pattern
# Theme: Car Settings Without Snapshots
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Before the Memento pattern existed, saving and restoring state was
#   done manually. The object had to expose its internal variables so
#   outside code could store and modify them. This breaks encapsulation
#   and couples external code tightly to the object's implementation.
#
#   In this BEFORE example, the driver tries to save car presets using
#   external variables instead of snapshots. Any internal change to the
#   CarSettings class instantly breaks all saved presets.
# ==============================================


# -----------------------------
# BEFORE: Car Settings (state exposed)
# -----------------------------
class CarSettings:
    # All internal state is public.
    # External code must manually read/write the values.
    def __init__(self):
        self.seat = 0
        self.mirrors = "neutral"
        self.ac = 20

    def set_settings(self, seat, mirrors, ac):
        self.seat = seat
        self.mirrors = mirrors
        self.ac = ac
        print(f"Settings applied → Seat:{seat}, Mirrors:{mirrors}, AC:{ac}")


# -----------------------------
# BEFORE: Saving presets manually (fragile)
# -----------------------------
def manual_save(car_settings):
    # External code extracts ALL internal fields manually.
    # If CarSettings changes internally, this breaks.
    print("Manually saving current settings...")
    return {
        "seat": car_settings.seat,
        "mirrors": car_settings.mirrors,
        "ac": car_settings.ac,
    }


def manual_restore(car_settings, saved_preset):
    # External code restores each variable manually.
    print("Manually restoring settings...")
    car_settings.seat = saved_preset["seat"]
    car_settings.mirrors = saved_preset["mirrors"]
    car_settings.ac = saved_preset["ac"]
    print(
        f"Restored → Seat:{car_settings.seat}, Mirrors:{car_settings.mirrors}, AC:{car_settings.ac}"
    )


# -----------------------------
# Example Usage (Before Memento)
# -----------------------------
# Demonstrating disadvantages
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE Memento Example (Car Settings) ---\n")

    car = CarSettings()

    # Apply comfort mode
    car.set_settings(70, "wide", 22)
    comfort_preset = manual_save(car)

    # Apply sport mode
    car.set_settings(40, "narrow", 18)
    sport_preset = manual_save(car)

    # Restore comfort mode
    print("# -----------------------------")
    print("# REAL-WORLD USAGE (restoring presets)")
    print("# -----------------------------")

    print(">>> Restoring comfort preset")
    manual_restore(car, comfort_preset)

    # Restore sport mode
    print(">>> Restoring sport preset...")
    manual_restore(car, sport_preset)

    print("# -----------------------------")
    print("# DISADVANTAGE DEMO (Manual Save/Restore Fails)")
    print("# -----------------------------")
    print(">>> Now the car receives a NEW internal field: 'steering' (simulating a software update)")
    car.steering = 5  # new field not covered by old presets

    print("Applying a new setting that includes 'steering'...")
    # Manual save CANNOT store this new field
    new_preset = manual_save(car)
    print(f"Saved preset (missing steering): {new_preset}")

    print(">>> Restoring old preset (notice steering is NOT restored!)")
    manual_restore(car, comfort_preset)
    print(f"Current steering value (should have been restored but wasn't): {car.steering}")


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE Memento Example (Car Settings) ---
# Settings applied → Seat:70, Mirrors:wide, AC:22
# Manually saving current settings...
#
# Settings applied → Seat:40, Mirrors:narrow, AC:18
# Manually saving current settings...
#
# >>> Restoring comfort preset...
# Manually restoring settings...
# Restored → Seat:70, Mirrors:wide, AC:22
#
# >>> Restoring sport preset...
# Manually restoring settings...
# Restored → Seat:40, Mirrors:narrow, AC:18
#
# NOTE:
#   This BEFORE version exposes internal details and is fragile.
#   Adding a new field (e.g., steering wheel height) requires changes in:
#       - CarSettings
#       - manual_save()
#       - manual_restore()
#   This is exactly what the Memento pattern fixes.
# ==============================================
# History
# ==============================================
# Before the Memento pattern was formalized by the Gang of Four,
# software that needed undo/redo or configuration snapshots relied on
# manually storing state in external variables. This tightly coupled
# external code to internal representations. Any change to internal
# fields broke all save/restore logic.
#
# The Memento pattern solved this by encapsulating snapshots inside
# a dedicated object. Only the originator can create and restore them,
# preserving full encapsulation.
# ==============================================
