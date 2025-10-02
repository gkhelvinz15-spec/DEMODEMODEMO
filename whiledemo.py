#while demo

import random
magic = random.randint(1, 100)

ans = int(input("enter a number between 1 and 100: "))
while ans != magic:
    if ans > magic:
        print("the number is too high")
    elif ans < magic:
        print("the number is too low")
    ans = int(input("enter a number between 1 and 100: "))
else:
    print("You guessed the number! Thanks for playing!")