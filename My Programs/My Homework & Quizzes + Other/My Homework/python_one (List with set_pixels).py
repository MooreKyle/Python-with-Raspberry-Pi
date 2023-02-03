#python_one (List with set_pixels).py
#Kyle Moore - Project 1

from sense_hat import SenseHat #Get library for Sense HAT Functionality
from time import sleep #Get library for Sense HAT Output Delays

def main(): #main() body
    
    sense = SenseHat() #Declaration & Initialization

    sense.clear() #Clear Sense HAT Output Display - Fresh Start just in case :)

    sense.show_message("Kyle Moore",scroll_speed=0.2,back_colour=[255,255,0],text_colour=[0,255,255]) #Display my First & Last Name w/ appropriate specs. via Sense HAT

    sense.clear()

    #Variable Declarations & Initialization
    b = [0,255,255] #blue
    y = [255,255,0] #yellow
    p = [160,32,240] #purple
    n = [0,0,0] #null

    pattern_list = [n,n,n,n,n,n,n,n,
                    n,n,n,b,n,n,b,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,y,n,n,
                    n,n,p,n,n,n,n,p,
                    n,n,n,p,p,p,p,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n]

    sense.set_pixels(pattern_list)
    
    sleep(3.0) #Display Smiley Face for 3 Seconds
    sense.clear()

    sleep(1) #Delay Before Displaying Characters of Name
    
    #Display single characters of name
    sense.show_letter("K",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sense.show_letter("y",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sense.show_letter("l",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sense.show_letter("e",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sense.show_letter("M",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sense.show_letter("o",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sleep(0.1) #clearly show consecutive "o" in name
    sense.show_letter("o",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sense.show_letter("r",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    sense.show_letter("e",text_colour=[255,0,0])
    sleep(0.4)
    sense.clear()
    
main() #Call main()
