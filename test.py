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

def f (x: float):
    return 1/x

recip = float('Inf')
try:
    recip = 1 / f(0)
    print("Finite result")
except ZeroDivisionError:
    raise ZeroDivisionError("f(x) is 0, so 1/f(x) is undefined") from ArithmeticError("Division by zero")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


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

    