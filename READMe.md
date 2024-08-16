# Exception Handling in Python

Exception handling is a crucial part of writing robust and error-free code. It allows a program to handle errors gracefully without crashing. This README provides an overview of basic exception handling concepts in Python.

## Basic Concepts

### The `try` Block
The `try` block lets you test a block of code for errors. If an error occurs, the code inside the `try` block stops executing and jumps to the `except` block.

```python
try:
    # Code that may raise an exception
    value = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("The number is not divisible by 0. Try another number.")
```

### The `except` Block
The `except` block catches and handles exceptions that occur in the `try` block. You can specify the type of exception to catch or use a generic `except` block to catch all exceptions.

```python
try:
    value = int("abc")
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("The number is not divisible by 0. Try another number.")
```