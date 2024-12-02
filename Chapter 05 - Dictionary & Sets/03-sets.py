# !!! Sets don't allows duplicate items

a = {1, 2, 3, 4, 1}
print(a)
print(type(a))

b = {}         # This will create an empty Dictionary and not an empty Set
c = set()      # It will create an empty Set