n = int(input("Enter the number: "))

mul_table= [n*i for i in range(1,11)]

for i, value in enumerate(mul_table):
    print(f"{n} x {i+1} = {value}")
