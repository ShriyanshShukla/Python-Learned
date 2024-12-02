class Employee:                      # Base or Parent or Super class
    company = 'ITC'
    salary = 1000000

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")                                                      

class Coder:
    language = 'Python'

    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder):   # Derived or Child class
    company = "ITC Infotech"

    def __init__(self, name):
        # super().__init__(name)
        self.name = name

    def showLanguage(self):
        print(f"The salary is {self.salary} and he is good with {self.language} language")     

a = Employee('Shriyansh')
b = Programmer('Harry')

b.show()
b.showLanguage()
b.printLanguages()