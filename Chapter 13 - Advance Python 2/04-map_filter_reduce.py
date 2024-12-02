from functools import reduce

# Map
l = [1, 2, 3, 4]

square = lambda x: x*x

sqlist = map(square, l)   
print(list(sqlist))

# map applies a function to all the items in an input_list

# Filter
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce
def sum(a, b):
    return a + b

mul = lambda x,y: x*y

print(reduce(mul ,l))