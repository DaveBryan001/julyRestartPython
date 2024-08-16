# File Handling in Python

File handling is an essential part of any programming language. Python provides several functions for creating, reading, updating, and deleting files. This README provides an overview of basic file handling operations in Python.

## Basic Operations

### Opening a File

To open a file, use the `open()` function. This function takes two arguments: the file name and the mode in which the file is to be opened.

```python
# Open a file for reading (default mode)
file = open("myFile.txt")

# Open a file for writing
file = open("myFile.txt", "w")

# Open a file for appending
file = open("myFile.txt", "a")

# Open a file for reading and writing
file = open("myFile.txt", "r+")
```

### Reading from a File

**To read the contents of a file, use the read(), readline(), or readlines() methods.**

```python
file = open("myFile.txt", "r")

# Read the entire file
content = file.read()

# Read one line at a time
line = file.readline()

# Read all lines into a list
lines = file.readlines()

file.close()
```

### Writing to a File

**To write to a file, use the write() or writelines() methods.**

```python
file = open("myFile.txt", "w")

# Write a single string
file.write("Hello, World!\n")

# Write multiple lines
lines = ["This is \n", "a multi-line\n", "string\n"]
file.writelines(lines)

file.close()
```
### Appending to a File

**To append content to an existing file, open the file in append mode (a).**

```python
file = open("myFile.txt", "a")

# Append a single string
file.write("This is an appended line.\n")

file.close()
```
### Closing a File

Always close a file after completing operations to free up system resources.

### Using with Statement

Using the with statement is a best practice for file handling as it ensures the file is properly closed after its suite finishes.

```python
with open("myFile.txt", "r") as file:
    content = file.read()
    # No need to explicitly close the file here
```