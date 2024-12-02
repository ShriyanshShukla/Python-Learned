num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the third number "))
num4 = int(input("Enter the fourth number "))

if num1>num2 and num1>num3 and num1>num4:
    print("First number is the Greatest")
elif num2>num1 and num2>num3 and num2>num4:
    print("Second number is the Greatest")
elif num3>num1 and num3>num2 and num3>num4:
    print("Third number is the Greatest")
else:
    print("Fourth number is the Greatest")