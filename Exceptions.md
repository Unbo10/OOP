# Exceptions

## Introduction

In most programming languages there are two main types of errors that can appear due to different reasons: compilation errors and runtime or execution errors. The first ones include syntax or parsing, logic and semantic errors, which refer to mistakes found by the parser implying that a piece of the code does not correspond to the selected language's valid syntax.

On the other hand, runtime or execution errors (better known as **bugs**) appear after the program has been compiled (so it doesn't have any of the previous errors). These encompass logic errors made by the programmer that allow the program to run but it returns an incorrect output due to a wrong reasoning and the main topic of this summary: exceptions.

> *Exceptions are runtime errors that stop the execution of the program because of unexpected behaviors. They are ***events or instances*** of abnormal situations that the programming language doesn't know how to handle*.

Notice the use of the word *instances*. Of course it has nothing to do with classes, errors must be a reserved keyword... right?

### Exceptions are objects

That's right, you read it correctly. Exceptions are in reality an instance of a class that inherit from a parent class. All the built-in exception classes inherit from the grand-parent class [``BaseException``](https://docs.python.org/3/library/exceptions.html#BaseException). Instantiating it requires a tuple of arguments (``args``) which store usually a single string to be returned with the type of error. Also, as an object, it has attributes and methods such as:
- the ``__traceback__`` attribute, which stores a traceback object. This is a key part of any exception since this object contains all the necessary information displayed in the console when an error is raised or appears. In other words, it allows us to track the error from where it happened inside a block (its root) to the last block it affects.
- the ``with_traceback(tb)`` method, which sets ``tb`` as the new instance to be used when inquiring about the error's traceback. It pretty much can redirect an error to a different location or even a different instance of another error.
- the ``__note__`` attribute, which is a tuple containing all the strings added via the method ``add_note()``. It will be returned along with the type of error and the string given in ``args``. The useful feature about it is you can add as many strings as you want, and all of them will be printed alongside ``args`` and the error type.
- the ``add_note(note)`` method, which adds the string ``note`` to the ``__note__`` attribute. It will therefore be returned and printed in the screen when the error is raised.

However, any non-exiting (non-fatal) or user-defined exception classes are derived directly from the [``Exception``] class, only ``GeneratorExit``, ``KeyboardInterrupt`` and ``SystemExit`` inherit directly from ``BaseException``, since they are exiting or system-related excepction classes. All the exceptions that may raise are listed [here](https://docs.python.org/3/library/exceptions.html#concrete-exceptions).

## Handling exceptions

Since exceptions are objects that indicate errors and not actual errors, they can be handled or managed using blocks of code that **catch** the exception and do something with it without exiting the program's execution. There are different structures to do so:

### The ``try-except`` block

This is the universal and most used way of handling exceptions. It does the same as the ``try-catch`` block of other languages, most notably C++ and Java. 

It works by executing the [``try``](https://docs.python.org/3/reference/compound_stmts.html#try)'s *clause* or *suite*, the block of code in between ``try`` and ``except``, to the end or until an exception occurs. In the former, no exception is found so the totality of the ``try``'s suite is executed and none of the ``except`` blocks are entered (no handler is required so the executions continues normally).

In the latter (when not all of the suite is executed), what's left to execute after the exception is skipped and the control flow will now stand at the ``except`` keyword and its following expression, which indicates the type of error the program is expected to handle and its name (modified using ``as``). If the expression specifies that the error to handle is exactly the same as the one that occured during the ``try``'s suite execution, then the ``except`` suite is executed, i.e., the error is handled; otherwise, the interpreter returns to the ``try`` suite and tries a different way of passing the exception to other handlers, simmilar to ``*args``, and if there is none to manage this error, then the exception becomes *unhandled*, and execution stops with an error message (in this case, an error *has* occured).

For example, the following script contains a ``try-except`` structure that handles errors related to the user's input (in case it is not the required type), and only terminates when a number has been entered:

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number. Try again...")
```

Note that, as said, once an error occurs, the remaining lines of the ``try``'s suite are ignored (otherwise, in the example, in any case it would exit the ``while`` cycle). That is the beauty and usfulness of ``try``: it is somewhat *an interpreter within the interpreter* that checks, inside a block of code, for runtime errors line-by-line, but doesn't end the execution if one appears, instead, it passes it to the respective handler which can do pretty much anything with it and after its suite execution the rest of the active script's lines are executed normally. 

It's like when a road is being paved: there is a steamroller that deals with any of the bumps that it is required to fix without stopping. It may pause the rest of the flattening process but it won't stop working because of the bump.

#### The ``except`` handlers

The steamroller can go over all the bumps or only certain bumps if it is told to do so. Simmilarly, an ``except`` statement may handle certain matching types of errors or any that are found. Therefore, three types of handlers can be implemented:

<table>

<tr>
<th style = "text-align: center"> <code>except:</code> </th>
<th style = "text-align: center"> <code>except E as e:</code> </th>
<th style = "text-align: center"> <code>except* E as e:</code> </th>
</tr>

<tr>
<td>Labeled as expression-less, it is the most basic form of handling: it handles any exception that could occur in the <code>try</code>'s suite. In consequence, it should be the last handler defined. </td>
<td>This type of handler matches only one occurrence of the type of error <code>E</code> that can be treated as <code>e</code> if the <code>as</code> keyword is used (otherwise, it will have to be referred to as <code>E</code>).</td>
<td>The group handler is the most powerful of the three. It is able to handle exception groups, i.e., multiple exceptions raised at the same time that are or inherit from <code>E</code>.</td>
</tr>
</table>

Note: Exception groups are instances -too- of the classes ``ExceptionGroup`` and/or ``BaseExceptionGroup``. They have [different methods](https://docs.python.org/3/library/exceptions.html#exception-groups) although pretty much the same attributes as ``Exception`` and ``ExceptionGroup``, respectively. If an error matches multiple blocks, it will be handled by the first one.

It should be noted that, in the same ``try`` structure, there cannot be handlers of exception groups and of single exceptions. Examples of ``except*`` can be found in its [documentation](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.derive):

### The ``else`` and ``finally`` blocks

The ``else``'s and ``finally``'s suites are optional in the ``try-except`` structure, but they can be quite handy in some cases:

- The ``else`` keyword indicates, in this context, that if the control flow does not enter any ``except`` or if it doesn't skip the structure (using ``return``, ``continue``, or ``break``), then do the following. Therefore, it will only execute when no exception has been handled and when the control flow has not been yet returned to the outisde code. It is suggested to be used when code needs to be added after the expected exception(s) inside the ``try``'s suite. It is better to include it inside the ``else``'s suite as different errors than the expected may occur in this extra code. For example:
  
  ```py
    def is_even(n: int) -> bool:
        if n % 2 == 0:
            return True
        else:
            return False
    def get_number() -> int:
        x = int(input("Please enter an integer number: "))
        return x

    try:
        n = get_number()
    except ValueError as e:
        e.add_note("Oops! It seems you haven't entered an integer number.")
        raise(e)
    else:
        print("Your number,", n, "is even?", is_even(x))
  ```

  As can be seen, the ``else``'s suite is just a continuation of ``try``'s: ``n`` can be accessed in both, although that should happen throughout the rest of the script as long as there is no errors and exceptions are handled correctly.

- The ``finally`` keyword introduces a *cleanup* handler. It is suppose to deal with any kind of exceptions that were not handled by any of the previous handlers. In addition, it will be executed whether the exceptions were handled or not, in contrast to ``else``. Also, it has quite a high hierarchy in terms of keywords, since it will be executed whether control flow change keywords (``return``, ``continue``, or ``break``) are present or not; if there are, ``finally``'s suite will be executed "on the way out" of the ``try`` structure. For example:
  
  ```py
    def foo():
        try:
            return 'try'
        finally:
            return 'finally'
    foo()
  ```
  
  Despite a return appearing, it will print "finally" anyway. Note that there is no ``except`` block. That's because there is not only ``try-except`` but also ``try-finally`` structures, since ``finally`` is a handler.

### The ``raise`` statement

It does literally what its name says: it raises an exception that has ocurred (It technically re-raises it as it was raised when it first occured). Internally though, it creates a ``traceback`` object that, as stated previously in this document, stores attributes related to the exception that are key to understand the context and the exception itself. To mention one, it has a ``__context__`` attribute to print a message in the console about what the current or active exception's type is.

Furthermore, it can be joined with ``from``, which changes some attributes in the ``traceback`` object of the exception raised, must notably, it supresses the ``__context__`` and gives priority to the ``__cause__`` attribute, which specifies the exception to which the active exception is linked to in a causal relationship to the exception written after ``from``. For example:

```py
def f (x: float):
    return 1/x

recip = float('Inf')
try:
    recip = 1 / f(0)
    print("Finite result")
except ZeroDivisionError:
    raise ZeroDivisionError("f(x) is 0, so 1/f(x) is undefined") from ArithmeticError("Division by zero")
```

When executed, in the console it raises the arithmetic error exception and "The above exception was the direct cause of the following exception:", followed by the ``traceback`` object which ends in the active exception's context.

### When should you handle exceptions and when shouldn't you do so


