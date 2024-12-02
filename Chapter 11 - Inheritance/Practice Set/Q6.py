class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, v2):
        result = Vector(self.i + v2.i, self.j + v2.j, self.k + v2.k)
        return result
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v1 = Vector(10, 20, 30)
v2 = Vector(11, 22, 33)

print(v1 + v2)