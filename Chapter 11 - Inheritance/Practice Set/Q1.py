class TwoD_Vector: 
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeD_vector(TwoD_Vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoD_Vector(1, 2)
a.show()
b = ThreeD_vector(3, 4, 5)
b.show