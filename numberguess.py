life= 3
Secret_number = 42
import random
guess = int(input("guess a number:"))
if guess == Secret_number:
    print("you win the game!")
else:
    life = life-1
    while life>0:
        guess = int(input("guess a number:"))
        if guess == Secret_number:
            print("you win the game!")
            break
        else:
            life = life-1
    if life == 0:
        print("You have 0 life left. game over!")