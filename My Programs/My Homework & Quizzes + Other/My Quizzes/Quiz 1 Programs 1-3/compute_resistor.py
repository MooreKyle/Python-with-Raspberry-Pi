#compute_resistor.py
#Kyle Moore - 5-29-19

from sense_hat import SenseHat

def main():

    #Declarations
    base_cost = 2.0
    sense = SenseHat()

    #Get resistors from user & display resistors via Sense HAT
    resistors = int(input("Please enter the number of resistors: "))
    sense.show_message("The number of resistors is ",scroll_speed=0.3,text_colour=[0,255,0],back_colour=[160,32,240])
    sense.clear()

    #Decision Structure - Compute cost based on user input
    if resistors >=1 and resistors <= 100:
        cost = (resistors * 2) + base_cost
    elif resistors >= 101 and resistors <= 1000:
        cost = (resistors * 1.755) + 1.5
    elif resistors >= 1001 and resistors <= 5000:
        cost = (resistors * 1.125) + 0.5
    else:
        cost = resistors * 0.925

    #Print cost
    print("The cost is: " + format(cost,".2f"))
    print("The cost is: " + format(cost,".1e"))
    
main()
