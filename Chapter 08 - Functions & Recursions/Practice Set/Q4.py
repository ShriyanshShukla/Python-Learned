def sum_of_natural(n):
    if n==1:
        return 1
    return n + sum_of_natural(n-1)

n = int(input("Enter the number: "))
print(f"The sum of {n} natural numbers is", sum_of_natural(n))