# Modules and Functions in Python

This script demonstrates different ways to import and use functions from a module in Python.

## Concepts Covered

### Functions

This script demonstrates basic Python functions for greeting users. The functions are defined in the [`test.py`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py)  module.
### `greet(name)`
This function takes a single argument `name` and prints a greeting message "hello" followed by the name.

**Example:**
```python
greet("Ben")
# Output: hello Ben
```

### Importing Functions

1. **Standard Import**:
    ```python
    from test import greet
    ```
    This line is commented out, but it shows the standard way to import a specific function ([`greet`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition")) from the [`test`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") module.

2. **Import with Alias**:
    ```python
    from test import greet as sayhello
    ```
    This imports the [`greet`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") function from the [`test`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") module and renames it to [`sayhello`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") within the current script.

3. **Import Entire Module**:
    ```python
    import test
    ```
    This imports the entire [`test`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") module, allowing access to all its functions using the [`test.`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") prefix.

4. **Import Another Function**:
    ```python
    from test import sayhi
    ```
    This imports the [`sayhi`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") function from the [`test`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") module.

### Using Imported Functions

1. **Calling a Function from the Imported Module**:
    ```python
    test.sayhi("Dave")
    ```
    This calls the [`sayhi`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") function from the [`test`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") module, passing `"Dave"` as an argument.

2. **Calling a Directly Imported Function**:
    ```python
    sayhi("Dave")
    ```
    This calls the [`sayhi`](https://github.com/DaveBryan001/julyRestartPython/blob/main/test.py "Go to definition") function directly, as it was imported without the module prefix.

### Importing Built-in Modules in Python

This [script](https://github.com/DaveBryan001/julyRestartPython/blob/main/math2.py) demonstrates basic mathematical operations using Python's `math` module. It includes examples of using the `fabs` and `floor` functions to perform absolute value and floor operations, respectively.

The script imports the `math` module and also imports the `fabs` function from the `math` module with an alias `f`.

```python
import math
from math import fabs as f
```

## Conclusion

This script illustrates various ways to import and use functions from a module in Python, providing flexibility in how you structure and call your code.