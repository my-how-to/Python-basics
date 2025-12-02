# ==============================================
# BEFORE — State Pattern
# Theme: Phone Sound Modes (Silent / Vibrate / Loud)
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Before the State pattern, an object changes its behavior using
#   long chains of if/elif statements. As new modes are added, every
#   method must be updated, making the code hard to maintain.
#
#   In this BEFORE example, a phone handles sound modes manually.
#   Adding a new mode breaks the logic and requires massive rewrites.
# ==============================================


# -----------------------------
# BEFORE: Phone with if/elif-based logic
# -----------------------------
class Phone:
    def __init__(self):
        self.mode = "silent"   # silent, vibrate, loud

    def set_mode(self, new_mode):
        print(f"Changing mode to: {new_mode}")
        self.mode = new_mode

    def receive_call(self):
        if self.mode == "silent":
            print("...no sound...")
        elif self.mode == "vibrate":
            print("Bzzzzz (vibrating)...")
        elif self.mode == "loud":
            print("Ring! Ring! (loud)")
        else:
            print("Unknown mode — cannot handle call.")

    def receive_notification(self):
        if self.mode == "silent":
            print("(silent notification)")
        elif self.mode == "vibrate":
            print("bzz (vibration)")
        elif self.mode == "loud":
            print("Ding! Notification sound!")
        else:
            print("Unknown mode — cannot handle notification.")


# -----------------------------
# Example Usage (Before State Pattern)
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE State Pattern Example (Phone Sound Modes) ---\n")

    phone = Phone()

    print("# -----------------------------")
    print("# BASIC USAGE")
    print("# -----------------------------\n")

    phone.receive_call()            # silent
    phone.set_mode("vibrate")
    phone.receive_call()            # vibrate
    phone.set_mode("loud")
    phone.receive_call()            # loud

    print("\n# -----------------------------")
    print("# DISADVANTAGE DEMO (New Mode Breaks Logic)")
    print("# -----------------------------\n")

    print("Adding new mode: 'airplane' (simulating a software update)")
    phone.set_mode("airplane")  # New mode not handled

    print("\n>>> Receiving a call in 'airplane' mode:")
    phone.receive_call()            # fails or prints "unknown mode"

    print("\n>>> Receiving notification in 'airplane' mode:")
    phone.receive_notification()    # fails or prints "unknown mode"


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE State Pattern Example (Phone Sound Modes) ---
#
# -----------------------------
# BASIC USAGE
# -----------------------------
# ...no sound...
# Changing mode to: vibrate
# Bzzzzz (vibrating)...
# Changing mode to: loud
# Ring! Ring! (loud)
#
# -----------------------------
# DISADVANTAGE DEMO (New Mode Breaks Logic)
# -----------------------------
# Adding new mode: 'airplane' (simulating a software update)
# Changing mode to: airplane
#
# >>> Receiving a call in 'airplane' mode:
# Unknown mode — cannot handle call.
#
# >>> Receiving notification in 'airplane' mode:
# Unknown mode — cannot handle notification.
#
#
# ==============================================
# History
# ==============================================
# Before the State pattern, developers handled changing behavior using
# if/elif chains. Each state variation required modifying many methods
# and introduced fragile logic. The State pattern emerged to replace
# branching with polymorphism, keeping behavior inside dedicated classes.
# ==============================================
