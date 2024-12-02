class Programmer:
    company = 'Microsoft'

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"Company: {self.company}\nThe name of employee is: {self.name}\nThe salary of employee is: {self.salary}\nThe language of employee is: {self.language}")

shri = Programmer('Shriyansh', 1000000, 'Python')
shri.getInfo()