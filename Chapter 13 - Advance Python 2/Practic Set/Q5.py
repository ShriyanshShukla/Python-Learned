from functools import reduce

l = [1, 2, 3, 4, 55, 6, 7]

def greater(a, b):
    if a>b:
        return a
    return b

print(reduce(greater, l))