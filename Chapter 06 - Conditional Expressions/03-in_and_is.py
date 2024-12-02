a = None
l = [23, 44, 69]

# It will print Yes if 69 is inside l
if 69 in l:
    print("Yes")
else:
    print("No")

#In Python, the == operator is used to compare the equality of two objects. the is operator is used to check whether two variables point to the same object in memory.
if a is None:
    print("Yes")
else:
    print("No")

# For example:
a = 1
b = 1

print(a == b)  # It is comparing if both values are 1 or not
print(a is b)  # It is comparing if both variables have 1 as a value or not