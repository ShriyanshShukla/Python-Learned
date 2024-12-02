class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):     
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)

# n.__add__(m)
# self refers to the object on the left-hand side 
# num is the object on the right-hand side 