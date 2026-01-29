# inheritance is a way of creating a new class from existing class.
# The new class inherits attributes and methods from the existing class,
# allowing for code reuse and the creation of more complex data structures.


class Employee:
    company = "Google"
    name = "Harry Bhai"
    def show(self):
        print(f"the name of emp is {self.name} and company is {self.company}")


class Programmer(Employee):
    company = "Microsoft"
    language = "Python"
    def showLanguage(self):
        print(f"the emploee {self.name} knows {self.language}")


emp1 = Employee()
prog = Programmer()

print(emp1.company,prog.company)

prog.showLanguage();


# inheritance are 3 types:
# 1. single inheritance - when a class inherits from only one parent class
# 2. multiple inheritance - when a class inherits from more than one parent class
# 3. multilevel inheritance - when a class inherits from another class, which in turn inherits from another class