a = 10
b = 0

try:
    print(a/b)

except ZeroDivisionError as z:
    z = 'Infinite'
    print(z)