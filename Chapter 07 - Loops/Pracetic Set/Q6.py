num = int(input("Enter the number: "))
fctrl = 1

for i in range(1,num+1):
    fctrl *= i

print(f"The factorial of {num} is {fctrl}")