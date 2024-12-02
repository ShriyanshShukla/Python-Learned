class Employee:               # Base or Parent or Super class
    company = 'ITC'

    def show(self):
        print(f"The name is {self.name}")                                                     # type:ignore

class Programmer(Employee):   # Derived or Child class
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.salary} and he is good with {self.language} language")      # type:ignore

a = Employee()
b = Programmer()

print(a.company, b.company)