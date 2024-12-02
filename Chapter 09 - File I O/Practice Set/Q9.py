file1 = 'this.txt'
file2 = 'copy.txt'

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Yes, Both files have identical content")
else:
    print("No, Both files have different content")