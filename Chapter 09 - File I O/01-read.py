# Use open function to read the contents of the file

f = open('sample_01.txt', 'r')          # By default the mode will be 'r'
data = f.read()                 # Reads all of the characters from the file
print(data)
f.close()                       # We can read the file only one time

f = open('sample_01.txt', 'r')
data = f.read(11)               # Reads the first 11 characters of the file
print(data)
f.close()

# Readline Function
f = open('sample_01.txt')
data = f.readline()             # It will read the first line of the file(Also includes \n)
print(data)
data = f.readline()             # It will read the second line of the file
print(data)
f.close()