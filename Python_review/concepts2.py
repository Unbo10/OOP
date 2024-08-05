import numpy

def function(a, b):
        return 0

def add(*arguments):
        print(arguments)
        print(sum(*arguments))
    # * (*name) returns a sequence with the parameters passed to the function
    # * and it is used in the function as a list of the arguments passed 

if __name__ == "__main__":
    n : int = int(input(""))
    flag = True

    while (flag) or (n < 5):
        flag = False
        print("Hello user!")
        n += 1
    # * This is a Python-equivalent to the C++ and other languages' do-while cycle, which guarantees
    # * that the code block inside the while will be executed at least once
        
    i : int = -2
    while True:
        if i == 0:
            print(i)
            continue
        elif i < 5:
            i += 2
        else:
            break
        print(i)
        i += 2
    # * break and continue allow for vulnerabilities to happen, so its use is not recommended
    # * break ends the cycle and continue skips to the next iteration
        
    cars: list = ["W15", "SF-24", "RB20"]
    for item in cars:
        print(item, end = " *** ")
    print()
    # * The for cycles iterates over a sequence (lists, tuples, dictionaries or sets),
    # * which means it will do something per item in the sequence
        
    for i in range(0, 6, 2):
        print(i, end=", ")
    print()
    # * range(a, b, c) generates a sequence containing all indexes from [a, b) with c steps
    # * in between each number, i.e., (a, a + c, a + 2c, ..., b - 2c, b - c)
    
    l1 : list = [[0, 1], 2, "HELLO", numpy.pi, True, 4.23, 0.8, "WORLD", False]
    l2 = [0, 2, 0, 8]
    l3: list = l1 + l2 # * List concatenation: adds all the elements of l2 at the end of l1, just like a str
    l4: list = l1 * 4 # * Multiplication also applies since it's just concatenating the same list n times
    l5: list = l1[1:6:2] # * Slicing: returns a list with the elements from start to stop with a step
    print("l5:", l5)
    l6: list = l1[::-1] # Steps can be negative, which means they will be taken in reverse
    print("l6:", l6)
    l7: list = l1[-2:]
    print("l7:", l7)
    l7 = l1[:-2] # * Stop and start with a negative index means to start counting from the last element to the first
    print("l7:", l7)
    l8 = l1[slice(1, 6, 2)] # * The slice function is equivalent to the slicing notation

    l1.append(1) # * Adds the element to the end of the list
    l1.insert(8, 2) # * Inserts the element at the index and shifts all the elements to the right including
    # * the one that was at [8]
    l1.pop(0) # * Removes the element at the index and returns it (you can assign it to a variable)
    l1.pop() # * Removes the last element of the list if no argument is passed   
    l1.remove(2) # * Removes the first occurrence of the element in the list
    l2.sort(reverse=True) # * Sorts the list in ascending order, and reverse=True sorts it in descending order

    is_prime = (lambda x: all(x % y != 0 for y in range(2, x)))
    primes = [is_prime(x=x) for x in range(2, 100) if (x < 50)]
    # * Expression to return | For an iterable | If a condition is met
    print("primes", primes)

    
    sums = (lambda x, y: x + y) # * A lambda function is a compressed function which only 
    # * takes arguments and returns a value, and it's defined in a single line
    subtraction = (lambda x, y: x - y)(1, 2) # * It can also be defined with the arguments in the same line
    print(sums(1, 2))
    print(subtraction)

    function (a = l1, b = l2) # * The arguments to pass to the function can be set with the
    # * name of the parameter so their order doesn't matter and mistakes are not made

    add((0, 1, 2, 3, 4))

    

