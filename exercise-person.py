class Person:
    def __init__(self, age: int = 0, name: str = "Pepito") -> None: # Parameters are not fixed, they just have a default value
        self.age = age
        self.name = name

    def greeting(self):
        print(self.name, "is greeting you!")

    def is_older_than(self, person) -> bool:
        if (self.age > person.age):
            return True
        else:
            return False
    
    specie: str = "Homo Sapiens Sapiens Sapiens"

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
