class Employee:
    company = "Google"
    name = "Harry Bhai"

    def show(self):
        print(f"the name of emp is {self.name} and company is {self.company}")


class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"the language is {self.language}")


class Programmer(Employee, Coder):
    company = "Microsoft"

    def showDetails(self):
        print(f"the emploee is {self.name} from {self.company} knows {self.language}")


prog = Programmer()

prog.showDetails()
