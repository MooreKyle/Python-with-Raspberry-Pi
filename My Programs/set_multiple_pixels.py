#set_multiple_pixels.py

from sense_hat import SenseHat
from time import sleep

def main():
    r = [255,0,0]
    g = [0,255,0]
    b = [0,0,255]

    sense = SenseHat()

    pattern_list = [r,r,r,r,r,r,r,r,
                    g,g,g,g,g,g,g,g,
                    g,g,g,g,g,g,g,g,
                    b,b,b,b,b,b,b,b,
                    g,g,g,g,g,g,g,g,
                    b,b,b,b,b,b,b,b,
                    r,r,r,r,r,r,r,r,
                    r,b,g,r,g,b,r,g]

    sense.set_pixels(pattern_list)
    sleep(5)
    sense.clear()
main()
