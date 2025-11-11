# ==============================================
# Adapter Pattern Example (Simple and Clear)
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# 
# Description:
#   This file demonstrates the Adapter Design Pattern
#   using a fun and easy-to-understand analogy:
#   a European charger that needs to work with a USA socket.
#
#   The Adapter pattern helps two incompatible interfaces
#   work together without changing their code.
#   It's like using a plug adapter when traveling abroad.
# ==============================================

# -----------------------------
# Old class (European charger)
# -----------------------------
class EuropeanCharger:
    def provide_power_eu(self):
        """Simulates providing power from a European outlet (220V)."""
        return "⚡ Power from European outlet (220V)"


# -----------------------------
# New class (USA socket)
# -----------------------------
class USASocket:
    def supply_power_usa(self):
        """Simulates providing power from a USA outlet (110V)."""
        return "🔌 Power from USA outlet (110V)"


# -----------------------------
# Adapter class
# -----------------------------
class PowerAdapter:
    """Adapter that allows a EuropeanCharger to be used with a USASocket."""

    def __init__(self, charger: EuropeanCharger):
        # Keep a reference to the object we're adapting
        self.charger = charger

    def supply_power_usa(self):
        """Translate the EU-style power output to USA standard."""
        return f"{self.charger.provide_power_eu()} adapted to USA standard!"


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    # Create the original (incompatible) object
    eu_charger = EuropeanCharger()

    # Wrap it with an adapter
    adapter = PowerAdapter(eu_charger)

    # Now it can work with the USA socket system
    print(adapter.supply_power_usa())

    # Output:
    # ⚡ Power from European outlet (220V) adapted to USA standard!


# ==============================================
# History
# ==============================================
# The Adapter pattern was first described in the
# 1994 book “Design Patterns: Elements of Reusable
# Object-Oriented Software” by the Gang of Four.
# 
# It was inspired by the real-world idea of electrical
# adapters — connecting incompatible systems without
# modifying them.
