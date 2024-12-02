def G_number(num1, num2, num3):
    if num1 > (num2 and num3):
        print(f"Number {num1} is the Greatest")
    elif num2 > (num1 and num3):
        print(f"Number {num2} is the Greatest")
    else:
        print(f"Number {num3} is the Greatest")

G_number(111,20,5)