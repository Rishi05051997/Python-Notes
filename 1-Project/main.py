import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 'w':
            return True
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