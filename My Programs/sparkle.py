#sparkle.py
from sense_hat import SenseHat
from time import sleep
from random import randint

def main():
    sense = SenseHat()
    try:
        while True:
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            x = randint(0,7)
            y = randint(0,7)
            sense.set_pixel(x,y,r,g,b)
            sleep(0.1) #0.1666667 is 60 fps
    except KeyboardInterrupt: #Ctrl+C is the default to exit
        print("Exiting")
    finally:
        sense.clear()

main()
