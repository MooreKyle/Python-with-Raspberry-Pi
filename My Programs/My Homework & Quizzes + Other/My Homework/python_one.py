#python_one.py
#Kyle Moore - Project 1

from sense_hat import SenseHat #Get library for Sense HAT Functionality
from time import sleep #Get library for Sense HAT Output Delays

def main(): #main() body
    
    sense = SenseHat() #Declaration & Initialization

    sense.clear() #Clear Sense HAT Output Display - Fresh Start just in case :)

    sense.show_message("Kyle Moore",scroll_speed=0.2,back_colour=[255,255,0],text_colour=[0,255,255]) #Display my First & Last Name w/ appropriate specs. via Sense HAT

    sense.clear()
    
    sense.set_pixel(3,1,[0,255,255]) #First Blue Eye
    sleep(0.3)
    sense.set_pixel(6,1,[0,255,255]) #Second Blue Eye
    sleep(0.3)
    sense.set_pixel(5,3,[255,255,0]) #Yellow Nose
    sleep(0.3)
    sense.set_pixel(2,4,[160,32,240]) #First End of Purple Mouth
    sleep(0.3)
    sense.set_pixel(3,5,[160,32,240]) #Bottom of Purple Mouth 1
    sleep(0.3)
    sense.set_pixel(4,5,[160,32,240]) #Bottom of Purple Mouth 2
    sleep(0.3)
    sense.set_pixel(5,5,[160,32,240]) #Bottom of Purple Mouth 3
    sleep(0.3)
    sense.set_pixel(6,5,[160,32,240]) #Bottom of Purple Mouth 4
    sleep(0.3)
    sense.set_pixel(7,4,[160,32,240]) #Second End of Purple Mouth

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
