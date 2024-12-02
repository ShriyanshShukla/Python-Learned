l = [3, 513, 53, 535]

index = 0
for item in l:
    index += 1
    print(f"The item number {index} is {item}")

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")

# Emunerate returns a tuple which include (index, value)