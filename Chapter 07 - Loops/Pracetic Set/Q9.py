n = int(input("Enter the number: "))

if n==1:
    print("*")
else:
    for i in range(1):
        print("*" * n)

        for j in range(n-2):
            if n%2==0:
                print("*" * int(n/2-1), end="")
                print(" " * 2, end="")
                print("*" * int(n/2-1))
            else:
                print("*" * int((n+1)/2-1), end="")
                print(" ", end="")
                print("*" * int((n+1)/2-1))

        print("*" * n)

    # for i in range(1):
    #     print("*" * n)

    #     for j in range(n-2):
    #         print("*", end="")
    #         print(" " * (n-2), end="")
    #         print("*")

    #     print("*" * n)