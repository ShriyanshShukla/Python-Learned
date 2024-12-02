def num():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return 'Something'

    except Exception as e:
        print(e)
        return 'Something'

    else:
        print("I am inside else")              # This code will only execute if there is no error and the code in try section had executed successfually

    finally:
        print("Hey I am insdie of finally")    # This code will always execute even if function has returned something

num()