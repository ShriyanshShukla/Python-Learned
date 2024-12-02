class calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"The square of {self.num} is: {self.num*self.num}")

    def cube(self):
        print(f"The cube of {self.num} is: {self.num**3}")

    def square_root(self):
        print(f"The square root of {self.num} is: {self.num**0.5}")

four = calculator(4)
four.square()
four.cube()
four.square_root()