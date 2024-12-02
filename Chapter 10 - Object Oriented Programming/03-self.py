class Employee:
    language = "Py"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")

    @staticmethod 
    def greet():
        print("Good Morning")

harry = Employee()
harry.greet()
harry.getInfo() 
harry.language = "Javascript"
Employee.getInfo(harry)

# Functions(Methods) in the class operates on an object and takes it as an argument that's why we use self variable as an argument receiver so we don't get an error and can also use object's attributes by using self as an reference