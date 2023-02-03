#led_pattern.py
#Kyle Moore - 5-29-19

#Libraries
from sense_hat import SenseHat
from time import sleep



#main body
def main():

    #Variable Declarations & Initialization
    p = [160,32,240] #purple
    b = [0,0,255] #blue
    n = [0,0,0] #null
    i = 1
    sense = SenseHat()

    sense.clear() #Fresh Start

    #Loop - Sense HAT LED Cartesian Plane blinking
    while i <= 3:
        pattern_list_1=[n,n,n,n,n,n,n,n,
                        n,n,b,b,n,n,n,n,
                        n,n,n,n,n,n,p,p,
                        n,n,n,n,n,n,n,n,
                        n,n,n,n,p,p,n,n,
                        n,n,n,n,n,n,n,n,
                        n,n,b,b,n,n,n,n,
                        n,n,n,n,n,n,n,n]

        pattern_list_2=[n,n,n,n,n,n,n,n,
                        n,n,n,n,n,n,n,n,
                        n,n,n,n,n,n,n,n,
                        n,n,n,n,n,n,n,n,
                        n,n,n,n,n,n,n,n,
                        n,n,n,n,n,n,n,n,
                        n,n,n,n,n,n,n,n,
                        n,n,n,n,n,n,n,n]

        sense.set_pixels(pattern_list_1)
        sleep(0.5)
        sense.set_pixels(pattern_list_2)
        sleep(0.5)
        i = i + 1
        
    sleep(3.0)
    sense.clear()

main() #Call main()
