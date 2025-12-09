# ===========================================
#  OOP BASICS — LESSON 3: INHERITANCE & POLYMORPHISM
# ===========================================
#
# Description:
#   Lesson 3 completes the OOP path with:
#   - multi-level inheritance and super()
#   - overriding vs extending behavior
#   - multiple inheritance with mixins
#   - built-in helpers (isinstance, issubclass, hasattr, getattr, setattr)
#   - polymorphic processing of collections
#   - capstone demo combining everything
#
# Run this file directly to see each concept logged in the terminal.
#

print("\n# -----------------------------")
print("# 1. MULTI-LEVEL INHERITANCE")
print("# -----------------------------\n")


class Device:
    def power_on(self):
        print("Device powering on")


class Computer(Device):
    def boot(self):
        print("Computer boot sequence initiated")


class Laptop(Computer):
    def open_lid(self):
        print("Laptop lid opened")


my_laptop = Laptop()
my_laptop.open_lid()
my_laptop.boot()
my_laptop.power_on()  # inherited from Device


# ===========================================
# 2. SUPER() AND METHOD OVERRIDING
# ===========================================

print("\n# -----------------------------")
print("# 2. SUPER() AND METHOD OVERRIDING")
print("# -----------------------------\n")


class NotificationService:
    def send(self, message):
        print(f"[Generic] {message}")


class EmailNotification(NotificationService):
    def send(self, message):
        super().send(message)  # call parent logic first
        print(f"[Email] {message}")


class SMSNotification(NotificationService):
    def send(self, message):
        print(f"[SMS] {message}")  # completely overrides without parent call


email = EmailNotification()
sms = SMSNotification()
email.send("Exam reminder!")
sms.send("Exam reminder!")


# ===========================================
# 3. MULTIPLE INHERITANCE & MIXINS
# ===========================================

print("\n# -----------------------------")
print("# 3. MULTIPLE INHERITANCE & MIXINS")
print("# -----------------------------\n")


class LogMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class PersistentMixin:
    def save(self):
        print("Saving object to storage...")


class BaseModel:
    def __init__(self, identifier):
        self.identifier = identifier


class UserModel(LogMixin, PersistentMixin, BaseModel):
    def __init__(self, identifier, username):
        BaseModel.__init__(self, identifier)
        self.username = username

    def change_username(self, new_name):
        self.log(f"Changing username from {self.username} to {new_name}")
        self.username = new_name
        self.save()


user = UserModel(101, "codex_student")
user.change_username("project_ready")


# ===========================================
# 4. isinstance(), issubclass(), hasattr()
# ===========================================

print("\n# -----------------------------")
print("# 4. BUILT-IN TYPE HELPERS")
print("# -----------------------------\n")


print("Is user an instance of UserModel?", isinstance(user, UserModel))
print("Is UserModel a subclass of BaseModel?", issubclass(UserModel, BaseModel))
print("Does user have 'username'?", hasattr(user, "username"))
print("Does Device have method 'boot'?", hasattr(Device, "boot"))


# ===========================================
# 5. getattr(), setattr(), delattr()
# ===========================================

print("\n# -----------------------------")
print("# 5. DYNAMIC ATTRIBUTE ACCESS")
print("# -----------------------------\n")


class DynamicExample:
    def __init__(self):
        self.name = "dynamic"


dyn = DynamicExample()
print("Initial name via getattr:", getattr(dyn, "name"))
setattr(dyn, "level", "intermediate")
print("New attribute level:", dyn.level)
delattr(dyn, "name")
print("Has name after delete?", hasattr(dyn, "name"))


# ===========================================
# 6. POLYMORPHIC COLLECTIONS
# ===========================================

print("\n# -----------------------------")
print("# 6. POLYMORPHIC COLLECTIONS")
print("# -----------------------------\n")


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 9)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area:", shape.area())


# ===========================================
# 7. CAPSTONE: SIMPLE TICKETING SYSTEM
# ===========================================

print("\n# -----------------------------")
print("# 7. CAPSTONE: SIMPLE TICKETING SYSTEM")
print("# -----------------------------\n")


class Ticket:
    next_id = 1

    def __init__(self, title, severity="low"):
        self.id = Ticket.next_id
        Ticket.next_id += 1
        self.title = title
        self.severity = severity
        self._resolved = False

    def resolve(self):
        self._resolved = True
        print(f"Ticket #{self.id} resolved.")

    def status(self):
        return "resolved" if self._resolved else "open"

    def __repr__(self):
        return f"Ticket(id={self.id}, title={self.title!r}, severity={self.severity!r})"


class BugTicket(Ticket):
    def __init__(self, title, steps):
        super().__init__(title, severity="high")
        self.steps = steps

    def details(self):
        return f"Bug: {self.title}\nSteps: {self.steps}"


class FeatureTicket(Ticket):
    def __init__(self, title, impact):
        super().__init__(title, severity="medium")
        self.impact = impact

    def details(self):
        return f"Feature: {self.title}\nImpact: {self.impact}"


class TicketBoard:
    """Uses composition to hold any ticket subclass."""

    def __init__(self):
        self._tickets = []

    def add_ticket(self, ticket):
        if not isinstance(ticket, Ticket):
            raise TypeError("Only Ticket instances are allowed")
        self._tickets.append(ticket)
        print(f"Added ticket #{ticket.id}: {ticket.title}")

    def resolve_high_priority(self):
        for ticket in self._tickets:
            if ticket.severity == "high" and ticket.status() != "resolved":
                ticket.resolve()

    def summary(self):
        for ticket in self._tickets:
            print(f"#{ticket.id} [{ticket.severity}] {ticket.title} → {ticket.status()}")


board = TicketBoard()
bug = BugTicket("Crash when saving", steps="Open app → Save → Crash")
feature = FeatureTicket("Dark mode", impact="Improves UX at night")
board.add_ticket(bug)
board.add_ticket(feature)
board.summary()
board.resolve_high_priority()
board.summary()


# ===========================================
# SUMMARY REMINDERS
# ===========================================
#
# - Multi-level inheritance shares behavior through the hierarchy.
# - Use super() when you want to extend parent behavior.
# - Mixins add reusable features; multiple inheritance should stay simple.
# - isinstance / issubclass help validate relationships at runtime.
# - getattr/setattr/delattr enable dynamic manipulation, but use carefully.
# - Processing collections of base-class references demonstrates polymorphism.
# - Build mini projects (like the ticket board) to combine every tool.
#
