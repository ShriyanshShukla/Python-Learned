a = int(input("Enter a first number: "))
b = int(input("Enter a secoond number: "))

if b == 0:
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division of a/b is {a/b}")