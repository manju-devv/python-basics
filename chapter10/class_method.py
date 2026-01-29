# A class method in Python is a method that is bound to the class, not the object (instance).
# It works with the class itself and can access/modify class variables, but not instance-specific data directly.


# 🔹 Definition
# A class method is defined using the @classmethod decorator,
# and it takes cls (class reference) as the first parameter instead of self


# ----> class method basically is a way to directly access class in a method


class Employee:
    a = 2

    def show(self):
        print(f"the class attribute is {self.a}")

    @classmethod
    def showClassMethod(cls):
        print(f"the class attribute {cls.a}")


e = Employee()
e.a = 99
e.showClassMethod()
e.show()





class Student:
    school_name = "Green Valley School"   # class variable

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


Student.change_school("Blue Ridge School")
print(Student.school_name)
