class Employee:
    a = 1


class Programmer(Employee):
    b = 2


class Manager(Programmer):
    c = 3


emp = Employee()
print(emp.a)

prog = Programmer()
print(prog.a, prog.b)

mgr = Manager()
print(mgr.a, mgr.b, mgr.c)




# Base class (Parent)
class Animal:
    def eat(self):
        print("Animal is eating")

# Child class (inherits Animal)
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Grandchild class (inherits Dog)
class Puppy(Dog):
    def play(self):
        print("Puppy is playing")

# Create object of Puppy
p = Puppy()

p.eat()    # from Animal
p.bark()   # from Dog
p.play()   # from Puppy









# Base class
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

    def eat(self):
        print(self.name, "is eating")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call Animal constructor
        self.breed = breed
        print("Dog constructor called")

    def bark(self):
        print(self.name, "is barking")

# Grandchild class
class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)  # call Dog constructor
        self.age = age
        print("Puppy constructor called")

    def play(self):
        print(self.name, "is playing")

# Object creation
p = Puppy("Tommy", "Labrador", 1)

p.eat()
p.bark()
p.play()
