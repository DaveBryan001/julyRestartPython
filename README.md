# Hello Script

This script demonstrates different ways to import and use functions from a module in Python.

## Concepts Covered

### Importing Functions

1. **Standard Import**:
    ```python
    from test import greet
    ```
    This line is commented out, but it shows the standard way to import a specific function ([`greet`](command:_github.copilot.openSymbolFromReferences?%5B%22greet%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A17%7D%7D%5D%5D "Go to definition")) from the [`test`](command:_github.copilot.openSymbolFromReferences?%5B%22test%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") module.

2. **Import with Alias**:
    ```python
    from test import greet as sayhello
    ```
    This imports the [`greet`](command:_github.copilot.openSymbolFromReferences?%5B%22greet%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A17%7D%7D%5D%5D "Go to definition") function from the [`test`](command:_github.copilot.openSymbolFromReferences?%5B%22test%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") module and renames it to [`sayhello`](command:_github.copilot.openSymbolFromReferences?%5B%22sayhello%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A26%7D%7D%5D%5D "Go to definition") within the current script.

3. **Import Entire Module**:
    ```python
    import test
    ```
    This imports the entire [`test`](command:_github.copilot.openSymbolFromReferences?%5B%22test%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") module, allowing access to all its functions using the [`test.`](command:_github.copilot.openSymbolFromReferences?%5B%22test.%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") prefix.

4. **Import Another Function**:
    ```python
    from test import sayhi
    ```
    This imports the [`sayhi`](command:_github.copilot.openSymbolFromReferences?%5B%22sayhi%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A17%7D%7D%5D%5D "Go to definition") function from the [`test`](command:_github.copilot.openSymbolFromReferences?%5B%22test%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") module.

### Using Imported Functions

1. **Calling a Function from the Imported Module**:
    ```python
    test.sayhi("Dave")
    ```
    This calls the [`sayhi`](command:_github.copilot.openSymbolFromReferences?%5B%22sayhi%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A17%7D%7D%5D%5D "Go to definition") function from the [`test`](command:_github.copilot.openSymbolFromReferences?%5B%22test%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") module, passing `"Dave"` as an argument.

2. **Calling a Directly Imported Function**:
    ```python
    sayhi("Dave")
    ```
    This calls the [`sayhi`](command:_github.copilot.openSymbolFromReferences?%5B%22sayhi%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22path%22%3A%22%2Fhome%2Fdavebryan%2Ftutorial%2Fhello.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A17%7D%7D%5D%5D "Go to definition") function directly, as it was imported without the module prefix.

## Conclusion

This script illustrates various ways to import and use functions from a module in Python, providing flexibility in how you structure and call your code.