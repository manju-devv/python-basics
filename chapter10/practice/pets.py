class Animals:
    def __init__(self, name):
        self.name = name
        print(f"your animal name is {self.name}")


class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)
        print(f"your pet name is {self.name}")


class Dog(Pets):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"your pet {self.name} is barking BOW! BOW!")


animal = Dog("Julio")
animal.bark()
