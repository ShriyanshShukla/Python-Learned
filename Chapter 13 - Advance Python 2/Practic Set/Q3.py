n = int(input("Enter the number: "))
mul_table = [str(n*i) for i in range(1, 11)]

s = '\n'.join(mul_table)
print(s)
