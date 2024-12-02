n = int(input("Enter the number: "))

for i in range(n):
    print(" " * (n-1-i), end="")
    print("*" * (2*(i+1)-1))

for i in range(n, 0, -1):
    print("*" * (2*i-1))
    print(" " * (n+1-i), end="")
# for i in range(n):
#     print("*" * (2*(n-i)-1))
#     print(" " * (n-(n-(i+1))), end="")

print("\n")
for i in range(n):
    print(" " * (n-1-i), end="")
    print("*" * (i+1))