# an object is instantiation of class. when class is defined
# a template is defined/created memory is allocated only after object is instantiated


# objects of a class can invoke methods available to it without revealing
# implementation details this is known as data hiding or encapsulation and encapsulation


class Employee:
    language = "Python"  # class attribute
    salary = 100000

    def getInfo(self):
        print(f"Employee Language is {self.language} and Salary is {self.salary}")

    # if we dont neet to send an entire object we can use static method
    @staticmethod
    def greet():
        print("Good Morning Employees")


harry = Employee()
harry.name = "Harry"  # this is an instance attribute
print(harry.name, harry.language, harry.salary)


# Instance attributes takes preference ovet class attributes if both are present with same name

zoro = Employee()
zoro.language = "JavaScript"
zoro.location = "India"
print(zoro.language, zoro.location, zoro.salary)
# print(Employee.location) # this will give error as location is not a class attribute
print(Employee.language)  # this will print class attribute value


zoro.getInfo()  # this will give error as getInfo method is not accepting any argument
# Employee.getInfo(zoro)  # internally conveted to this way by python interpreter
# and no need to pass object reference explicitly so we use self keyword


emp = Employee()
emp.greet()  # calling static method without creating object is also possible
emp.getInfo()
