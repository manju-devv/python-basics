class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square is {self.num**2}")

    def cube(self):
        print(f"the cube is {self.num**3}")

    def squareRoot(self):
        print(f"The square root is {self.num**(1/2)}")

    @staticmethod
    def greet():
        print("Welcome to the Calculator program")


cal = Calculator(9)
cal.greet()
cal.square()
cal.cube()
cal.squareRoot()
