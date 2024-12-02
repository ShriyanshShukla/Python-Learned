with open('sample_03.txt', 'w') as f:
    f.write("I am not writing")

with open('sample_03.txt') as f:
    a = f.read()

print(a)

# Now we don't need to use close function