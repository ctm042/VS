### More on Classes ###
if False:
    class Vehicle:
        def __init__(self,name):
            self.owner = name
            self.tires = None
            self.engine = None

        def __str__(self):
            return f"owner = {self.owner}, tires = {self.tires}, engine = {self.engine}"

    class Car(Vehicle):
        def __init__(self, name):
            super().__init__(name)
            self.tires = 4
            self.engine = True

        def __str__(self):
            return f"Car; {super().__str__()}"

    class Cycle(Vehicle):
        def __init__(self, name):
            super().__init__(name)
            self.tires = 2

    class Bicycle(Cycle):
        def __init__(self, name):
            super().__init__(name)
            self.engine = False

        def __str__(self):
            return f"Bicycle; {super().__str__()}"

    class Motorcycle(Cycle):
        def __init__(self, name):
            super().__init__(name)
            self.engine = True

        def __str__(self):
            return f"Motorcycle; {super().__str__()}"

    ### instances ###
    c1 = Car("Fred")
    b1 = Bicycle("Alex")
    m1 = Motorcycle("Jane")
    print(c1)
    print(b1)
    print(m1)

### List functions ###
if False:
    def f(x):
        return x**2+3
    print(f(3))

    # lambda function
    y = lambda x : x**2+3
    print(y(3))

    # filter a list of numbers from 1 to 10 and only print the even numbers
    print(list(filter(lambda x : x % 2 == 0, range(1,11))))

    # use the map function to square every element in the list
    print(list(map(lambda x : x ** 2, range(1,11))))

    # use the reduce function to return the product of all list elements
    from functools import reduce
    print(reduce(lambda x, y : x + y, range(1,6)))

### Sets ###
if False:
    print("sets")
    a = {1,2,3,4,5}
    b = {4,5,6,7,8}

    print(a | b) # a or b
    print(a & b) # a and b
    print(a - b) # elements in a that are not in b

    c = [2,4,6,8,10]
    d = set(c)
    print(c)

    e = "CSC132"
    f = set(e)
    print(f)

### Dictionaries ###
if False:
    cars = {"Fred":"Beetle", "Jane":"Tesla", "Jimmy":"Ferrari", "Bryce":"Ford F-150"}
    print(cars)

    #change a value
    cars["Bryce"] = "Jeep Gladiator"
    print(cars)

    #remove a key-value pair
    del cars["Jane"]
    print(cars)

    #add a key-value
    cars["Fish"] = "1997 Fish Bowl"
    print(cars)

    #iterate through values in the dictionary
    for k in cars.keys():
        print(k, ":", cars[k])

    for k, v in cars.items():
        print(k, ":", v)

### List & Dictionary Comprehension ###
if True:
    squares = [x * x for x in range(1,10) if x % 2 != 0]
    print(squares)

    squares_dict = {x : x * x for x in range(1,10) if x % 2 != 0}
    print(squares_dict)
