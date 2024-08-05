## Definitions worth knowing

* **Git**: Version control system.
* **Compiler**: Program that translates the entire source file into binary or object code and then makes the computer execute it (faster).
* **Interpreter**: Program that translates and executes the code line by line (easier to debug).
* **IDE**: Integrated Development Environment, is an application that has multiple software-development tools integrated into it. It is what spreadsheets are to accountants.
* **Editor**: A standalone application to write code. It has multiple tools to write better code more efficiently.

# Python review

## Basic code structure

1. Function definitions.
2. Global-variable and constant declarations.
3. Main function definition and call using `if __name__ == "__main__":` to avoid multiple calls to different main() in different files.

## Functions

An interesting way of viewing them is from Math's POV: they are pieces of code which have a **domain** (data types of the arguments) and a **range** (return value). So they assign an element from the input set (domain, arguments) an element of the output set (return value). Graphically, it is something like this: {} -> ▢ -> {}.

In Python, the `def` keyword is used to define a function, plus, you can add `-> data type:` after the arguments to set the function's range like this:

```py
def get_squared_number(x) -> float:
    return x * x
```

> Suggestions:
> - The fewer arguments the better (objects help a lot with this).
> - Each function should execute one action (abstract minor processes).
> - Use snake_case.

## Variables

They are actually a **memory location** that is pointed at by an identifier and where some data is stored. The identifiers are the words to name or refer to your variables (use snake_case), like `route_direction`, and *'hide'* the memory locations, while the data stored is the value *assigned* to the variable.

Since Python is not too strongly-typed, you don't need to specifiy the variables' types, but you can do so -and it is strongly recommended- using `: data type` after the identifier:

```py
num_fact = 10 #Essential declaration
num_fact = int(10) #Declaration with the value assigned being casted
num_fact : int = 10 #Declaration specifying the data type of the variable
```
The use of the `global` keyword is not encouraged, since it could cause troubles with variables holding the same identifiers as the global variable  defined. Only constants maintained throughout the entirety of the code may have a global scope.

## Terminal tricks

- `Ctrl + L` to clean the terminal.
- `Ctrl + C` or `Ctrl + Z` to stop the execution of any program.
- `Ctrl + R` to make a "back search", which searches for previously-written commands in the terminal.
- `Shift` to paste something from the clipboard, though at least in Windows `Ctrl + V` also works (definitely not in Linux though).

## Decorators

Decorators came up as a push to make code more readable with regard to 'nested calls' of functions, i.e., passing functions as arguments of other functions. Before them, calls were done after a function declaration, which meant their ultimate functionality was not present at first. Decorators made this possible with a rather strange syntax:

```py
@decorator
def func():
    pass
```

Using the ``@`` symbol and the name of the 'decorator function', you can use the wrapped function `func` as an argument of the decorator function.

It is useful when adding functionality to functions, especially inside classes. For example, the ``@classmethod`` decorator is used to define a class method, which passes the class itself as an argument rather than an instance of the class; whilst the ``@staticmethod`` decorator is used to define a static method, which does not pass the class or instance and is supposed to make a specific behavior related to the class but that doesn't require access to it or any of its instances.



