class Demo:
    def __new__(self):
        self.__init__(self)
        print("Demo's __new__ method is called")
    def __init__(self) -> None:
        print("Demo's __init__ method is called")

class DerivedDemo(Demo):
    def __new__(self):
        print("DerivedDemo's __new__ method is called")
    def __init__(self) -> None:
        print("DerivedDemo's __init__ method is called")

def main():
    obj1 = DerivedDemo()
    obj2 = Demo()
main()