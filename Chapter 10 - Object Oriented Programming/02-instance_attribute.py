class Employee:
    language = "Py"
    salary = 1200000

harry = Employee()
harry.language = "Java" 
print(harry.language, harry.salary) 

# Instance attribute take preference over the class attribute
