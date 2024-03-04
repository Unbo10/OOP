
# * Inheritance is a way to lend or borrow code from a class to another, so you don't have to write the same code again and again. It in consequence allows you to create a family of classes in which the children (derived classes) inherit attributes and methods from the parent(s) (base) class(es) that are in turn now part of them. Therefore, if you create an object of a derived class it will have all the attributes and methods of the parent class as well as of its own class.

# * super(Type, object_or_type = none) is a proxy object, i.e., a copy of the self() object of the base or parent class that lends or delegates method calls and attribute access to the object of Type (the instance of a child or derived class).

# *

class Person:
   def __init__(self, age: int = 0, name: str = "Pepito") -> None: # Parameters are not fixed, they just have a default value
      self.age = age
      self.name = name

   def greeting(self):
      print(self.name, "is greeting you!")
   
   def speak(self):
      print("Hello from", self.name)

   def is_older_than(self, person) -> bool:
      if (self.age > person.age):
         return True
      else:
         return False
   
   specie: str = "Homo Sapiens Sapiens Sapiens" # * Class attributes: Remain unchanged in every instance of the class

class Student(Person):
   def __init__(self, age: int = 0, name: str = "Pepito", ID: int = 0) -> None:
      super().__init__(age, name) 
      # * super() refers to the base class instance, like the self of it, and you can call all the methods and attributes from it in the subclass, including the initializer
      # ! You must call the bass class initializer in a subclass, since otherwise you won't have an instance of the bass class (super) to use in the subclass, so there wouldn't be inheritance
      self.id = ID
   def studying(self):
      super().speak()
      print(self.name, "is stu-dying 💀")

# Example of multiple inheritance:

class A:
   print("In class A: Grandparent")
   pass
class B:
   print("In class B: Grandparent")
class C (A, B):
   print("In class C: parent")
class D (A, B):
   print("In class D: parent")
class E (D, C):
   print("In class E: child")

print(A.__mro__) # Shows the MRO in reverse order (from the top to the bottom of the inheritance tree)

# Here, E inherits everything from its two parents, D and C, and they in turn inherit from their parent A, so E has everything from A, B, C and D. However, the order at the time of accessing an attribute or method using super(), for example, is from left to right and from the bottom to the top (refer to the OOP-rectangle.md). This is the way the Method Resolution Order (MRO) works in Python: using the C3 linearization algorithm, it travels all of the classes in the same abstraction level in the order they are declared (from left to right) and then it goes to the next level of abstraction (from bottom to top) and so on.
# ! However, you need to be careful with how do you declare multiple inheritance, because classes of the same level must have the same parent order for the MRO to work, since it supresses equal calls in the same order from different children. Otherwise, there will be a copy of the same class in the MRO, which is not allowed.
# For example, C and D have the same parent in the same order (A, B), so there won't be two copys of A and B in the MRO of E, but if you change the order of the parents in C and D, there will be two copys of A and B in the MRO of E, which is not allowed.

if __name__ == "__main__":
   Jesus = Person(age = 18, name = "Jesus")
   Jesus.greeting()

   user_name:str = str(input("Now insert your name please: "))
   user_age:int = int(input("and your age please: "))
   Other = Person(age = user_age, name = user_name)

   oldest: bool = Other.is_older_than(Jesus)
   if oldest == True:
      print("Congratulations {}! You are older than {}".format(Other.name, Jesus.name))
   else:
      print("{} is as old or older than you, {}!".format(Jesus.name, Other.name))

   student_oop: str = str(input("Please insert your name:"))
   student_age: int = int(input("and your age please: "))
   student_id: int = int(input("and your student id: "))
   StudentOop = Student(age = student_age, name = student_oop, ID = student_id)
   StudentOop.studying()
