#sense_hat_fun.py
from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    sense.set_pixel(2,1,255,0,0) #x,y,red,green,blue
    sleep(0.5)

    sense.clear()

main()
