# Python, Design Patterns — Educational Examples

This repository contains a collection of **simplified, commented examples** of classic *Object-Oriented Design Patterns* implemented in Python.

---

## Overview

The goal of this repository is to help learners understand **why** design patterns exist,
and **how** they improve code readability, flexibility, and maintainability.

Each file is self-contained and can be run directly using Python 3.

> **Note:** For simplicity, all files are stored in a single folder.
> Patterns are grouped by type (**Creational**, **Structural**, **Behavioral**) only in this README for easier navigation.

---

## Repository Structure

```
design_patterns/
│
├── factory_before.py
├── factory_registry.py
├── factory.py
├── singleton_before.py
├── singleton.py
├── ....
└── README.md
```

---

## How to Run

1. Clone the repository  

```bash
git clone https://github.com/my-how-to/patterns.git
cd patterns
```
2. Each file can be executed individually:

```bash
python3 factory_method_basic.py
python3 observer_before.py
python3 singleton_pattern.py
```

All examples include printed **Example Output** in the code itself,
so you can easily compare expected and actual behavior.

---

## Included Patterns

| Category       | Pattern        | Description                                             |
| -------------- | -------------- | ------------------------------------------------------- |
| **Creational** | Factory Method | Creates objects without specifying exact classes        |
|                | Singleton      | Ensures a class has only one instance                   |
| **Structural** | Adapter        | Bridges incompatible interfaces                         |
|                | Decorator      | Dynamically adds functionality to objects               |
| **Behavioral** | Observer       | Enables communication between objects via notifications |

---

## Educational Approach

Each pattern follows the same structure:

1. **Before Version** — shows the problem or repetitive code developers faced before the pattern.
2. **Pattern Version** — demonstrates the structured, reusable solution.
3. **Comments** — clear explanations in every file.
4. **Example Output** — real console output for better understanding.
5. **History** — short background on how and when the pattern appeared.

---

## ⚠️ Disclaimer

The code examples in this repository are **simplified educational demonstrations**
of design patterns. They are intended to explain key concepts clearly and concisely.

These examples **should not be used in production systems**
without additional error handling, optimization, and security considerations.

---

## Author

**Alexandru Petrenco.**
Educational repository built with AI assistance from *OpenAI GPT-5*.
This project is part of a personal study collection on **Object-Oriented Programming** and **Software Design Patterns**.
