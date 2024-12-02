import random

def game():
    return random.randint(1,100)

a = game()
with open('hi-score.txt', 'r') as f:
    b = f.read()

if b == '':
    with open('hi-score.txt', 'w') as f:
        f.write(str(a))
elif a > int(b):
    with open('hi-score.txt', 'w') as f:
        f.write(str(a))