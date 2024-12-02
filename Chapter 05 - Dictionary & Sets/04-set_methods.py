s = set()

# Adding values to an empty set
s.add(5)
s.add(4)
s.add(22)
s.add(33)
s.add('shri')
print(s)            

# s.add([9, 8, 7])  # We can't add a list inside an Set because it is changeble

s.add((8, 9, 7))    # We can add a tuple inside an Set because it is unchangeble
print(s)

s.remove(4)         # It will remove an given item from a Set
print(s)            

print(s.pop())      # It will remove and returns an random item from a Set

s.clear()           # Empties a Set
print(s)

a = {1, 8, 2, 3, 11}
b = {8}

print(a.intersection(b))   # It will return only duplicate items
print(a.union(b))          # it will return all the items 