# def obtener_elemento(lista, indice):
#   if indice < 0 or indice >= len(lista):
#     raise IndexError("Índice fuera de rango.") # Instantiates a certain class of error with a message, which will then be printed in the except block
#   return lista[indice]

# try:
#   elemento = obtener_elemento([1, 2, 3], 4)
#   print(f"El elemento en la posición 4 es: {elemento}")
# except IndexError as error:
#   print(f"Error: {error}")

  # A repeated except is not an exception but an if (it is too common to be treated as an exception)

  # Three cases of tries in challenge 6

# try:
#     print(1 / 0)
# except Exception as exc:
#     raise RuntimeError("Something bad happened") #from exc

# try:
#     raise ZeroDivisionError("Division by zero")
# except Exception as exc:
#     # print(exc.__traceback__)
#     exc.add_note("It has something to do with the operation inside the print statement")
#     exc.add_note("fewawfwe")
#     raise exc

# def f (x: float):
#     return 1/x

# recip = float('Inf')
# try:
#     recip = 1 / f(0)
#     print("Finite result")
# except ZeroDivisionError:
#     raise ZeroDivisionError("f(x) is 0, so 1/f(x) is undefined") from ArithmeticError("Division by zero")

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# def is_even(n: int) -> bool:
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# def get_number() -> int:
#     x = int(input("Please enter an integer number: "))
#     return x

# try:
#     n = get_number()
# except ValueError as e:
#     e.add_note("Oops! It seems you haven't entered an integer number.")
#     raise(e)
# else:
#     print("Your number,", n, "is even?", is_even(x))

# from collections import namedtuple

# Bibliotecas = namedtuple("Biblioteca", "Libros", ["estanterias", "libros"], ["autor", "año", "titulo"])

# Unal = Bibliotecas("Antoine", "1943", "El principito") # namedtuples can only be initialized with one type of object, so only one class name and one list of attributes can be passed as arguments


class Foo:
    class_counter: int = 0

    def __init__(self, instance_variable):
        self.instance_v = instance_variable

    def print_class_counter(self):
        print(__class__.class_counter)

    def increase_class_counter(self):
        Foo.class_counter += 1 
        # * Inside instance methods, both the class name and the __class__ attribute can be used
      
    def increase_instance_counter(self):
        self.instance_v += 1

    def print_instance_counter(self):
        print(self.instance_v)
    
    @classmethod
    def decrease_class_counter(cls):
        cls.class_counter -= 1

foo1 = Foo(5)
print(foo1.instance_v) # * 5
foo1.instance_v += 10
print(foo1.instance_v) # * 15
foo1.print_class_counter()  # * 0
foo1.increase_class_counter()
foo1.print_class_counter()  # * 1
foo1.decrease_class_counter()
foo1.print_class_counter()  # * 0

for i in range(1, -5, -1):
    Foo.decrease_class_counter()
    print(Foo.class_counter)

foo1 = Foo(0)
i = 0
while i < 10:
    foo1.increase_instance_counter()
    i += 1
foo1.print_instance_counter()  # * 10

