# ============================================================
#   @property — PYTHON PROPERTY DECORATOR
# ============================================================
# This file explains how the @property decorator works, including:
#   • turning methods into attributes
#   • creating getters, setters, and deleters
#   • computed / read-only properties
#   • validation inside setters
#   • practical real-world examples
#
# Everything is explained with clear, runnable examples.


# ============================================================
# 1. BASIC @property (GETTER)
# ============================================================

"""
@property allows you to access a method AS IF it were an attribute.

Benefits:
    • cleaner API
    • hide implementation details
    • compute values on demand
"""

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Return the temperature in Celsius (read-only)."""
        return self._celsius

    @property
    def fahrenheit(self):
        """Computed property — no need to store it."""
        return (self._celsius * 9/5) + 32


# ============================================================
# 2. GETTER + SETTER
# ============================================================

"""
Use a setter when you want to validate or transform data
before assigning it.
"""

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value


# ============================================================
# 3. GETTER + SETTER + DELETER
# ============================================================

"""
A deleter allows custom cleanup when an attribute is deleted.
"""

class SecureData:
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        if len(value) < 5:
            raise ValueError("Token too short")
        self._token = value

    @token.deleter
    def token(self):
        print("[SECURITY] Token has been deleted")
        del self._token


# ============================================================
# 4. READ-ONLY PROPERTIES
# ============================================================

"""
A property without a setter becomes read-only.
Useful for values that should never be modified publicly.
"""

class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username


# ============================================================
# 5. COMPUTED PROPERTIES
# ============================================================

"""
Properties can compute values dynamically.
No need for stored attributes.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


# ============================================================
# 6. PRACTICAL REAL-WORLD EXAMPLE
# ============================================================

"""
Properties are perfect for API-like class design.
They make the public interface clean and intuitive.
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Cannot set negative balance")
        self._balance = amount

    @property
    def is_empty(self):
        return self._balance == 0


# ============================================================
# 7. BEFORE vs AFTER — WHY @property IS USEFUL
# ============================================================

"""
This section explains WHY @property is better than traditional getter/setter methods.
Using the Temperature example, we compare:
    • BEFORE (classic get/set methods)
    • AFTER (clean @property API)
    • what happens when you add validation later
"""

# BEFORE @property (old style)
class TemperatureBefore:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        # no validation originally — risky
        self._celsius = value

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32


# AFTER @property (clean, Pythonic)
class TemperatureAfter:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32


"""
IMPORTANT INSIGHT ABOUT SETTERS:

When you write:

    @celsius.setter
    def celsius(self, value):
        ...

The name BEFORE `.setter` (here: celsius) MUST match the name of the property.
This works because @property turns the method into a PROPERTY OBJECT.

So this:

    @property
    def celsius(...)

Creates:

    celsius = property(<getter>)

And this:

    @celsius.setter

Is actually calling:

    celsius = celsius.setter(<setter_function>)

Meaning:
    “Attach this setter to the existing property called celsius.”

This keeps the public API clean:
    t.celsius        # get
    t.celsius = 25   # set (with validation)

While still hiding internal details like _celsius.
"""

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    # 1. Basic property
    t = Temperature(20)
    print(t.celsius, "C")
    print(t.fahrenheit, "F")

    # 2. Getter/Setter
    p = Person("Alex")
    p.name = "John"
    print(p.name)

    # 3. Getter/Setter/Deleter
    s = SecureData("abcde12345")
    print(s.token)
    del s.token

    # 4. Read-only
    u = User("alex_user")
    print(u.username)

    # 5. Computed properties
    r = Rectangle(5, 3)
    print("Area:", r.area)
    print("Perimeter:", r.perimeter)

    # 6. Real example
    acc = BankAccount(100)
    print("Balance:", acc.balance)
    acc.balance = 50
    print("Is empty?", acc.is_empty)
