class Employee:
    salary = 1000000
        
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary*0.5)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1) * 100

shriyansh = Employee()
shriyansh.salaryAfterIncrement = 1500000
print(shriyansh.increment)