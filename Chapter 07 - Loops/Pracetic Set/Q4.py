n = int(input("Enter the number: "))

prime = True
for i in range(2,n):
    if n%i == 0:
        prime = False
if prime:
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")