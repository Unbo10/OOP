def hello_function() :
    print("Hello")

# * Using the "->" operator you can specifiy the variable type to return
def get_squared_number(x) -> float:
    return x * x

""" 
# * Functions and variables with snake_case
# * Objects and clases with Pascal Case 
"""

""" 
    * Python is not too-strongly static typed, which means it doesn't
    * need the type of the variable to be declared, but it can be
    * using ":" followed by the data type. It is highly recommended
"""
boolean_variable: bool = True
integer_variable: int = 8
float_variable: float = 2.7186
text = "String" 

# * global variables are not encouraged, since it may cause
# * troubles while using them inside functions

#! This syntax forces the code to start here, since there could
#! be many main() among different files
if __name__ == "__main__":

    choice = input("")
    # * The match-case structure is the same as the switch-case in C++
    match choice:
        case "Hello":
            print("World")
        case "World":
            print("Hello")
        case _:
            print("a")


