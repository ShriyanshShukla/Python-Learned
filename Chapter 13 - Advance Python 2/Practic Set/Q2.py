name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
pho_num = int(input("Enter your phone number: "))

format = lambda name,marks,pho_num: print(f"The name of the student is {name}, his marks are {marks} and phone number is {pho_num}")

format(name, marks, pho_num)