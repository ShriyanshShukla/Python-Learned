name = 'Shriyansh'
greeting = "Good Morning, "
print(type(name))

# Concatenating
c = greeting + name        
print(c)
print('\n')

# Indexing and Negative Indexing
print("***Indexing and Negative Indexing***")
print(name[0], name[3], name[5])
print(name[-1], name[-3], name[-5])
print('\n')

# Slicing
print("***Slicing***")
print(name[1:5])     # It will only print string from Index 1 to 4
print(name[3:8])
print(name[:5])      # Same as name[0:5]
print(name[3:])      # It will print string to the end
print('\n')

# Slicing with negative Index
print("***Slicing with negative Index***")
print(name[-5:-3])
print(name[-9:])
print('\n')

# Slicing with Skip value
print("***Slicing with Skip value***")
print(name[0:5:1])
print(name[0:5:2])
print(name[-9:-2:2])
print(name[-4:-7:-1])
print(name[-4:-7:-2])
print(name[::-1])