def stars(n):
    for i in range(n):
        print("*" * (n-i))
    
    for i in range(n):
        print("*" * (n-i))
        print(" " * (i+1), end="")

n = int(input("Enter the number: "))
stars(n)