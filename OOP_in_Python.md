# Object-oriented Programming in Python

## Attributes

Attributes are data or information that belong to the object. They represent a property or characteristic of an object of a class. Furthermore, they can hold different values depending on its type.

### Class Attributes

These is the data all instances of a class will have in common. They are declared outside of the constructor method and cannot be modified using instance accessing (object.variable), so they will therefore be constant (unless there is a class method or a method that uses ____class__ __ or the class name to modify them).

```python
class Foo:
    class_counter: int = 0

    def __init__(self):
        pass

    def print_class_counter(self):
        print(__class__.class_counter)

    def increase_class_counter(self):
        Foo.class_counter += 1 
        __class__.class_counter += 1
        # * Inside instance methods, both the class name and the __class__ 
        # * attribute can be used to access class attributes.
    
    @classmethod
    def decrease_class_counter(cls):
        cls.class_counter -= 1

foo1.print_class_counter()  # * 0
foo1.increase_class_counter()
foo1.print_class_counter()  # * 1
foo1.decrease_class_counter()
foo1.print_class_counter()  # * 0
```

When using class methods (identified by the decorator ``@classmethod``), the first argument will be the class itself, which is usually named cls. It is therefore not a proxy object but a 'proxy class' that can be used to access class attributes. Also, any class method can be executed without the need for an instance of the class.

```python
for i in range(1, -5, -1):
    Foo.decrease_class_counter()
    print(Foo.class_counter)
```

### Instance Attributes

These is the data to instantiate alongisde an object of a class. They are defined in the constructor method using the self keyword. They can be modified using instance accessing (object.variable) and are unique to each instance of the class.

```python
class Foo:
    def __init__(self, instance_counter: int):
        self.instance_counter = instance_counter

    def print_instance_counter(self):
        print(self.instance_counter)

    def increase_instance_counter(self):
        self.instance_counter += 1

foo1 = Foo(0)
i = 0
while i < 10:
    foo1.increase_instance_counter()
    i += 1
foo1.print_instance_counter()  # * 10
```

### Warning with duck-typing

When you asume an object will have an attribute just because it belongs to certain class you can end up creating an instance of an attribute that was not part of the class. This is indeed an attribute instance, but it cannot be used inside any method defined in the class. In adition, it will ignore any class attribute with the same name, so accessing it will return a different value than the one assigned in the class.

```python
class Foo:
    class_counter: int = 0

    def __init__(self):
        pass

    def print_class_counter(self):
        print(__class__.class_counter)

foo1 = Foo()
foo1.class_counter = 10
foo1.print_class_counter()  # * 0
print(foo1.class_counter)  # * 10
```

Even if the attribute is defined in the class as an instance attribute, any instance of the class will have a different value for that attribute, because it is not anymore the class attribute.
    
```python
class Foo:
    class_counter: int = 0

    def __init__(self, instance_counter: int):
        self.instance_counter = instance_counter

    def print_instance_counter(self):
        print(self.instance_counter)

    def print_class_counter(self):
        print(__class__.class_counter)

foo1 = Foo(6)
foo1.print_instance_counter()  # * 6
foo1.print_class_counter()  # * 0
```


