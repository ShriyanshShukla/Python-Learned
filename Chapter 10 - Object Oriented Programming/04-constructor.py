class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name):   # Dunder(double underscore) method is automatically called
        print("I am creating an object")
        self.name = name

    def getInfo(self):
        print(f"The name is {self.name}.\nThe language is {self.language}.\nThe salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee("Hari")
rohan = Employee("Rony")
harry.getInfo()
rohan.getInfo()