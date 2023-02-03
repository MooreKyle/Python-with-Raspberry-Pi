#HILO_game.py
from random import randint

def main():
    computer = randint(1,1000) + 1 # 1 to 1000
    guess = int(input("Enter your guess 1 to 1000")) # priming read
    count = 0
    while guess != computer:
        if guess < computer:
            print("LO")
        elif guess > computer:
            print("HI")
        guess = int(input("Enter your guess 1 to 1000")) # loop read
        count += 1
    print("You won with {0:d} guesses!".format(count))

main()
