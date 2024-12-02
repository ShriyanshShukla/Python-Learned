def factorial_normal(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

def factorial_recursion(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursion(n-1)

print(factorial_recursion(0))
