class Animals:
    @staticmethod
    def bark():
        print("woof, woof")

class Pets(Animals):
    pass

class Dogs(Pets):
    pass

pitbull = Dogs()
pitbull.bark()