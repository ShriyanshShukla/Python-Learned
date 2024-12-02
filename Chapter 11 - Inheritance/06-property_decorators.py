class Employee:

    @property
    def name(self):
        return f"{self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(' ')[0]
        self.lname = value.split(' ')[1]

e = Employee()
e.name = 'Shriyansh Shukla'
print(e.name)
print(e.fname)
print(e.lname)