# The @property decorator allows you to access a method like an attribute (variable), without using parentheses.


class Employee:
    a = 1

    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self, value):
        self.ename = value


e = Employee()
e.name = "manju"
print(e.name)
