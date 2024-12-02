def Multiplication_table(n):
    print("Here is the Multiplication table of", n)
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter the number: "))

Multiplication_table(n)