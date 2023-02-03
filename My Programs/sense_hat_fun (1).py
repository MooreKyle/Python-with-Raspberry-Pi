#sense_hat_fun.py
from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    sense.set_pixel(2,1,255,0,0) #x,y,red,green,blue
    sleep(0.5)
    sense.set_pixel(1,2,0,0,255)
    sense.set_pixel(1,3,0,0,255)
    sense.set_pixel(1,4,0,0,255)
    sense.set_pixel(1,5,0,0,255)
    sleep(3)
    sense.set_pixel(4,2,0,255,0)
    sense.set_pixel(5,2,0,255,0)
    sense.set_pixel(6,2,0,255,0)
    sense.set_pixel(7,2,0,255,0)
    sleep(3)
    sense.set_pixel(0,0,0,255,255) #cyan
    sense.set_pixel(7,7,255,0,255) #magenta
    sleep(3)
    sense.clear()

main()
