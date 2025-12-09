# ===========================================
#  OOP BASICS — LESSON 2: BUILDING BETTER CLASSES
# ===========================================
#
# Description:
#   Lesson 2 expands your OOP toolkit with:
#   - flexible constructors and keyword-only args
#   - readable object representations
#   - class/instance/static methods
#   - encapsulation with properties
#   - composition vs inheritance
#   - practice section tying concepts together
#
# Goal:
#   Be comfortable designing slightly larger classes, hiding details cleanly,
#   and following Pythonic conventions for interview/cert exam readiness.
#

print("\n# -----------------------------")
print("# 1. FLEXIBLE CONSTRUCTORS")
print("# -----------------------------\n")


class Student:
    """Constructor with defaults + keyword-only arguments."""

    def __init__(self, name, cohort="Python Basics", *, active=True):
        self.name = name
        self.cohort = cohort
        self.active = active

    def suspend(self):
        self.active = False
        print(f"{self.name} is now inactive.")

    def summary(self):
        status = "active" if self.active else "inactive"
        return f"{self.name} ({self.cohort}) → {status}"


alex = Student("Alex")
sara = Student("Sara", cohort="Evening Track", active=False)
print(alex.summary())
print(sara.summary())
alex.suspend()
print(alex.summary())


print("\n# -----------------------------")
print("# 2. OBJECT IDENTITY & REFERENCES")
print("# -----------------------------\n")


class CoursePlan:
    """Shows how multiple names can point to the same object."""

    def __init__(self, title):
        self.title = title
        self.modules = []

    def add_module(self, name):
        self.modules.append(name)

    def __repr__(self):
        return f"CoursePlan(title={self.title!r}, modules={self.modules!r})"


plan = CoursePlan("Intro Sprint")
alias = plan              # alias references the same object
independent = CoursePlan("Intro Sprint")

alias.add_module("Loops")  # affects plan too
print("plan is alias?", plan is alias)
print("plan modules:", plan.modules)
print("independent modules:", independent.modules)
print("IDs:", id(plan), id(alias), id(independent))


def add_topic(course, topic):
    """Functions receive the reference, so mutations are shared."""
    course.add_module(topic)


add_topic(plan, "Functions")
print("Modules after helper call:", plan.modules)
print("alias sees same change:", alias.modules)
print("independent unaffected:", independent.modules)


print("\n# -----------------------------")
print("# 3. __str__ VS __repr__")
print("# -----------------------------\n")


class Book:
    """Demonstrates human vs developer friendly displays."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"


python101 = Book("Python 101", "Mike", 320)
print(str(python101))          # user-friendly
print(repr(python101))         # debugging friendly
print([python101])             # uses repr internally


print("\n# -----------------------------")
print("# 4. INSTANCE/CLASS/STATIC METHODS")
print("# -----------------------------\n")


class ProgressTracker:
    attempts = 0  # class attribute shared by everyone

    def __init__(self, student):
        self.student = student
        self.completed_modules = 0

    def mark_complete(self):
        """Instance method → uses specific object's data."""
        self.completed_modules += 1
        ProgressTracker.attempts += 1
        print(f"{self.student} completed module #{self.completed_modules}")

    @classmethod
    def total_attempts(cls):
        """Class method → works with class-level state."""
        return cls.attempts

    @staticmethod
    def passing_score(score):
        """Static method → utility tied to the class conceptually."""
        return score >= 70


tracker = ProgressTracker("Alex")
tracker.mark_complete()
tracker.mark_complete()
print("Total attempts so far:", ProgressTracker.total_attempts())
print("Is 65 passing?", ProgressTracker.passing_score(65))
print("Is 85 passing?", ProgressTracker.passing_score(85))


print("\n# -----------------------------")
print("# 5. ENCAPSULATION WITH PROPERTIES")
print("# -----------------------------\n")


class TemperatureSensor:
    """Hide internal representation but expose clean API."""

    def __init__(self, celsius=0):
        self._celsius = celsius  # leading underscore hints "internal use"

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


sensor = TemperatureSensor(25)
print("Celsius:", sensor.celsius)
print("Fahrenheit:", sensor.fahrenheit)
sensor.celsius = 30
print("Updated Celsius:", sensor.celsius)


print("\n# -----------------------------")
print("# 6. COMPOSITION VS INHERITANCE")
print("# -----------------------------\n")


class Engine:
    def start(self):
        print("Engine starting...")


class MusicSystem:
    def play(self, song):
        print(f"Playing {song}")


class Vehicle:
    def drive(self):
        print("Vehicle is moving")


class SmartCar(Vehicle):
    """Inherits drive behavior but composes other helpers."""

    def __init__(self):
        self.engine = Engine()
        self.music = MusicSystem()

    def go_for_drive(self):
        self.engine.start()
        super().drive()
        self.music.play("Chill Vibes")


assistant_car = SmartCar()
assistant_car.go_for_drive()


print("\n# -----------------------------")
print("# 7. PRACTICE MINI CHALLENGE")
print("# -----------------------------\n")


class QuizQuestion:
    """Use everything learned: repr, property, classmethod."""

    questions_created = 0

    def __init__(self, prompt, answer, difficulty="easy"):
        self.prompt = prompt
        self._answer = answer
        self.difficulty = difficulty
        QuizQuestion.questions_created += 1

    def __repr__(self):
        return f"QuizQuestion(prompt={self.prompt!r}, difficulty={self.difficulty!r})"

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if not value:
            raise ValueError("Answer cannot be empty")
        self._answer = value

    @classmethod
    def created_count(cls):
        return cls.questions_created


q1 = QuizQuestion("What does OOP stand for?", "Object-Oriented Programming")
q2 = QuizQuestion("Which method initializes new objects?", "__init__", difficulty="medium")
print(q1)
print(q2)
print("Stored answer:", q1.answer)
q1.answer = "Object Oriented Programming"
print("Updated answer:", q1.answer)
print("Total questions created:", QuizQuestion.created_count())


# ===========================================
# SUMMARY THOUGHTS
# ===========================================
#
# - Object variables store references; aliasing means one mutation can
#   affect all names pointing at the same object.
# - Constructors can combine positional, defaulted, and keyword-only params.
# - __str__ shows a friendly string; __repr__ is for developers.
# - Instance methods work on data; class/staticmethods add alternate behaviors.
# - Properties control attribute access without changing the attribute API.
# - Favor composition for "has-a" relationships; inherit only when behavior
#   truly needs to be shared.
# - Practice tying features together (like QuizQuestion) to build exam-ready intuition.
#
