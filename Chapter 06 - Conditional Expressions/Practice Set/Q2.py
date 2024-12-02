sub1 = int(input("Enter the marks of first subject: "))
sub2 = int(input("Enter the marks of second subject: "))
sub3 = int(input("Enter the marks of third subject: "))

total = (sub1+sub2+sub3)/3

if sub1>=33 and sub2>=33 and sub3>=33 and total>=40:
    print("Passed")
else:
    print("Failed")