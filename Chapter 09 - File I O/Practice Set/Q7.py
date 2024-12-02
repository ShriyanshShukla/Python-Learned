with open('log.txt') as f:
    a = f.read()

l = a.split('\n')
i = 0
for word in l:
    i += 1
    if 'python' in word:
        break

print(f"The word 'python' is presented in the line number of {i}")