# ==============================================
# Pattern Name: State
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   The State pattern lets an object change its behavior when its
#   internal state changes — as if the object becomes a different class.
#   In this example, a phone switches between sound modes:
#       SilentMode, VibrateMode, LoudMode.
#   Each state encapsulates its own behavior for receiving calls
#   and notifications.
#
# What Makes It Unique:
#   Instead of using if/elif chains, each state is a full object
#   containing its own behavior. Adding new modes no longer requires
#   editing Phone methods — you simply add a new state class.
# ==============================================


# -----------------------------
# State Interface
# -----------------------------
class PhoneState:
    def receive_call(self):
        raise NotImplementedError

    def receive_notification(self):
        raise NotImplementedError


# -----------------------------
# Concrete States
# -----------------------------
# NOTE:
#   If a NEW mode is added (e.g., AirplaneMode), ONLY these things change:
#       1. Create a new state class (e.g., class AirplaneMode(PhoneState))
#       2. Implement receive_call() and receive_notification() inside it
#       3. Switch to it using: phone.set_state(AirplaneMode())
#   No changes are required in:
#       - Phone class
#       - Other state classes
#   This is the main advantage over the BEFORE version.

# -----------------------------
class SilentMode(PhoneState):
    def receive_call(self):
        print("...no sound (silent mode)...")

    def receive_notification(self):
        print("(silent notification)")


class VibrateMode(PhoneState):
    def receive_call(self):
        print("Bzzzzz (vibrating)...")

    def receive_notification(self):
        print("bzz (vibration)")


class LoudMode(PhoneState):
    def receive_call(self):
        print("Ring! Ring! (loud)")

    def receive_notification(self):
        print("Ding! Notification sound!")


# -----------------------------
# Context (Phone)
# -----------------------------
class Phone:
    # The phone delegates behavior to its current state.
    def __init__(self):
        self.state = SilentMode()  # default mode

    def set_state(self, new_state):
        print(f"Changing state to: {new_state.__class__.__name__}")
        self.state = new_state

    def receive_call(self):
        self.state.receive_call()

    def receive_notification(self):
        self.state.receive_notification()


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    print("--- State Pattern Example (Phone Sound Modes) ---\n")

    phone = Phone()

    print("# -----------------------------")
    print("# USING DIFFERENT SOUND MODES")
    print("# -----------------------------\n")

    # Default: silent
    phone.receive_call()

    # Switch to vibrate
    phone.set_state(VibrateMode())
    phone.receive_call()

    # Switch to loud
    phone.set_state(LoudMode())
    phone.receive_call()


# -----------------------------
# Example Output
# -----------------------------
# --- State Pattern Example (Phone Sound Modes) ---
#
# -----------------------------
# USING DIFFERENT SOUND MODES
# -----------------------------
# ...no sound (silent mode)...
# Changing state to: VibrateMode
# Bzzzzz (vibrating)...
# Changing state to: LoudMode
# Ring! Ring! (loud)
#
#
# ==============================================
# History
# ==============================================
# The State pattern was introduced to replace large conditional blocks
# that controlled behavior based on an object's internal status. By
# turning each state into a dedicated class, software becomes easier to
# extend and modify — new states can be added without touching existing
# logic, improving maintainability and following the Open–Closed Principle.
# ==============================================
