n = int(input("Enter the number: "))

mul_table= [n*i for i in range(1,11)]

with open('Tables.txt', 'w') as f:

    for i, value in enumerate(mul_table):
        f.write(f"{n} x {i+1} = {value}\n")
