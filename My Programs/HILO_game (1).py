#HILO_game.py
from random import randint

def main():
    computer = randint(1,1000) + 1 # 1 to 1000
    guess = int(input("Enter your guess 1 to 1000")) # priming read
    count = 0
    limit_guesses = 13
    while guess != computer:
        if guess < computer:
            print("LO")
        elif guess > computer:
            print("HI")
        guess = int(input("Enter your guess 1 to 1000")) # loop read
        #guess = randint(1,1000)
        count += 1
        if count >= limit_guesses:
            break
    if count < limit_guesses:
        print("You won with {0:d} guesses!".format(count))
    else:
        print("You did not guess the correct number")
main()
