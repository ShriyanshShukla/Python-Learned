class Employee:
    language = "Py"        # This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Hari" # This is an instance(object) attribute         # type: ignore 
print(harry.name, harry.language, harry.salary)                     # type: ignore

rohan = Employee()
rohan.name = "Rony"                                                 # type: ignore
print(rohan.name, rohan.salary, rohan.language)                     # type: ignore

# Here name is object attribute and salary and language is class attributes as they directly belong to the class