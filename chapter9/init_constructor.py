# __init__() is a special method in Python classes, known as the constructor.
# It is automatically called when a new instance of a class is created.
# The primary purpose of the __init__() method is to initialize the attributes of the newly created object.
# it takes self argument and other arguments that are passed during object creation.


# Magic methods, also known as dunder methods (short for "double underscore"),
# are special methods in Python that begin and end with double underscores (__).
# These methods are invoked automatically by Python in response to specific operations, such as arithmetic, comparisons, or object initialization.
# They allow developers to customize the behavior of objects and enable operator overloading, making classes more intuitive and Pythonic.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(
            "This is a constructor method,creating an object of Student class"
        )  # dunder method

    def getDetails(self):
        print(f"name: {self.name}, age: {self.age}")


stud = Student("Harry", 34)
stud.getDetails()
