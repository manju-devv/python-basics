# super() is used to access the methods of super class in derived class


class Employee:
    def __init__(self):
        print("this is Employee constructor")

    a = 1


class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("this is Programmer constructor")

    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("this is Manager constructor")

    c = 3


emp = Employee()
print(emp.a)

prog = Programmer()
print(prog.a, prog.b)

mgr = Manager()
print(mgr.a, mgr.b, mgr.c)
