import random

def game(comp, you):
    # if two value are equal declare a tie
    if comp == you:
        return None
    # if computer = Snake
    elif comp == 's':
        # if I have Water then Computer win
        if you == 'w':
            return False
        # if I have Gun then I win
        elif you == 'g':
            return True
    # If Computer is having Water
    elif comp == 'w':
        # If I have gun then computer win
        if you == 'g':
            return False
        # If I have Snake then I win
        elif you == 's':
            return True
    # If Computer is having Gun
    elif comp == 'g':
        # If I have water then I win
        if you == 'w':
            return True
        # I have Snake then computer win
        elif you == 's':
            return False


print("Computer Turn : Snake(s) Water(w) or Gun(g)?")
randomNo = random.randint(1,3)
if randomNo == 1:
    comp = 's'
elif randomNo ==2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g) ?")

a = game(comp, you)

print(f"computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print('The game is tie')
elif a:
    print('You win')
else:
    print('You lose ')