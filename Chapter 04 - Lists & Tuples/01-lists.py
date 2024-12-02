# !!! Lists are changeble

# Creating a list
a = [1, 2, 3, 4, 5, 6]
print(a)
print(a[1], a[5])

# Modifying a list
a[0] = 7
print(a[0])

# We can also create a list with different types of items
b = [45, 5.8, 'Shri', True]
print(b)

# List slicing
friends = ['Harry', 'Tom', 'Rohan', 'Sam', 'Divya', 45]
print(friends[0:4]) 
print(friends[-4:])
print(friends[-2::-1])

a[1:3] = [8,9]
print(a)