with open('log.txt', 'r') as f:
    a = f.read()

if 'python' in a:
    print("Yes!")
else:
    print("No!")