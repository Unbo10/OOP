# * Objects are only present in execution time. Classes are the code, so it doesn't depend on the program's execution.

# * Instantiating is a great way to reuse code: using classes you can have multiple objects that share the same code so you don't need to 

# * Two types of attributes: of a class (defined inside the class' body, belongs to all the instances/objects and doesn't change depending on the instance -- properties with a set-by-default value) and of an instance (different for each object)

# * Using the __init__ method, you can create a pseudo-instance or a default instance (self) which will set default values to instance (and not class) attributes, which can then be accessed and modified by every instance later created.

# * self is a reference to the object that is being instantiated. self is actually the instance of an object being self-conscious without the object even existing!! It therefore can be used as an object, with all its attributes and methods, inside the class.

class Point:
    definition: str = "Abstract unit that represents a location in space"
    def __init__(self, x = 0, y = 0): # Initializer, simmilar to constructors
        print("Initializer")
        self.x = x
        self.y = y
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point) -> float:
        return ((self.x - point.x))**0.5


point1 = Point(x = 1, y = 3) # This is instantiating an object; creating a class
point2 = Point(x = 0, y = 0)
print(point1.definition, point2.definition) # Class attribute: doesn't deppend on the object and it is inherited by all of them
print("Point 1:", point1.x, point1.y)
print("Point 2:", point2.x, point2.y)

point1.move(point1, 2, 5)
point2.move(-1, -1) # The point2 argument is not necessary since it is the object calling the method
print("After moved, point 1:", point1.x, point1.y)
print("After moved, point 2:", point2.x, point2.y)

