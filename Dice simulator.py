import random

function = str(input("What function do you want to do?"))
if function == "Roll a dice" or "roll a dice":
    rolled = random.randint(0, 6)
    print("The number that was randomly generated is", rolled)

elif function == "Flip a coin" or "flip a coin":
    flipped = random.randint(0,1)
    if flipped == 0:
        print("You got heads")
    else:
        print("You got Tails")

