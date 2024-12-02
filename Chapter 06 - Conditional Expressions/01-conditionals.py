# if-else statement ladder 
a = 45
if a>3:
    print("The value of a is greater than 3")
elif a>7:
    print("The value of a is greater than 7")
elif a>12:
    print("The value of a is greater than 12")
elif a>55:
    print("The value of a is greater than 55")
else:
    print("The is not greater than any provided values")

# Multiple if statements
b = 77
if b>3:
    print("The value of a is greater than 3")
if b>7:
    print("The value of a is greater than 7")
if b>12:
    print("The value of a is greater than 12")
if b>55:
    print("The value of a is greater than 55")
else:
    print("The is not greater than any provided values")

# Difference:-
# Multiple if statements can be less efficient than using elif. This is because each if statement has to be evaluated, even if the first one evaluates to True. With elif, only the first statement that evaluates to True is executed.