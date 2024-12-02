import random

n = random.randint(1,100)

class Guess:
    def __init__(self, player):
        self.num = player
        
        for i in range(1,10):
            if self.num == n:
                print("Congrats!! Your Gusess was correct")
                print(f"Number of guesses you made: {i}")
                break
            elif self.num < n:
                self.num = int(input("Higher Number Please: "))

            elif self.num > n:
                self.num = int(input("Lower Number Please: "))
        else:
            print("You have used all number of guesses")

player = int(input("Choose a number between 1 to 100: "))
Guess(player)