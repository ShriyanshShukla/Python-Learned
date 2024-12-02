import random

def swk(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        else:
            return False

comp = ''
randNO = random.randint(1,3)
if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

you = input("Choose: Snake(s), Water(w) or Gun(g):-\n")
a = swk(comp, you)

print(f"You chose {you} and Computer chose {comp}")
if a == None:
    print("It's a DRAW!")
elif a:
    print("You Win!")
else:
    print("You Lose!")