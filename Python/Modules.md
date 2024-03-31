# Modules (and packages)

A module in Python is actually... an object! It acts as something like the super() or self objects but of an external directory or file, compressed or not. It is most often a set of files and directories (although not always, since .zip files can also be imported and these do not have the usual file system organization) that contain blocks of code or more files, respectively.

> *A module is an **object** that acts as an organizational unit within another file.*
>
> That's why they have attributes like ``__path__`` or ``__name__``, which intend to facilitate the access to what they store via namespaces.

A file module contains definitions of functions and classes, and could even contain its own ``__main__``, just as an average ``.py`` file. On the other hand, a package module contains module files and/or subpackages, i.e., the path to them. Furthermore, the only difference between file and package modules is the ``__path__`` attribute that the latter has: it specifies the paths to the modules and subpackages it may contain.

## Importing

Modules gain considerable relevance when aiming at modularity, simplicity and reusability of code, because when you're in need of a function from another file, or need to create an object you had defined in a different project in a different directory, modules' importing is there to save the day.

It essentially consists in calling a function known as ``__import__()``. This function searches for a module's path using a simplified name and, if it matches any, it returns them and binds (fastens or secures) a name to it, which will in turn become a namespace in the file you're currently working on while simultaneously acting as a proxy object.