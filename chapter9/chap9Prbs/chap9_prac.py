class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getInfo(self):
        print(
            f"Hi i'm {self.name}. I work at {self.company} with salary of {self.salary}"
        )


p1 = Programmer("Harry", 100000)
p1.getInfo();
p2 = Programmer("Rohan", 50000)
p2.getInfo();
