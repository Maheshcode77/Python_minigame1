
# Snake_Water_Gun or Rock_Paper_Scissors

import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp =='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp =='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp =='g':
        if you=='s':
            return False
        elif you=='w':
            return True



comp=input("Comp Turn: Sanke(s) Water(w) or Gun(g) ? press enter")

randNo=random.randint(1,3) #produce random int from 1 to 3
#print(randNo)

if randNo==1:
    comp='s'

elif randNo==2:
    comp='w'

elif randNo==3:
    comp='g'
b=input("Your's Turn: Sanke(s) Water(w) or Gun(g) ?")

a=gameWin(comp, b)

print(f"Computer choose: {comp}")
print(f"You choose: {b}")


if a==None:
    print("the game is a tie!")
elif a:
    print("you Win..!")
else:
    print("you Lose...!")