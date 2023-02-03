#conditionals_one.py
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    answer = input("Do you want to see the pressure? ")
    if answer.startswith("y") or answer.startswith("Y"): # yes, yeah
    #if answer.lower() == "y":
        pressure = sense.get_pressure()
        sense.show_message("The pressure is {0:5.2f} millibars".
                           format(pressure),scroll_speed=0.05,
                           back_colour=[100,100,100],text_colour=
                           [0,255,0])
        sense.clear()
    else:
        humidity = sense.get_humidity()
        sense.show_message("The humidity is {0:5.2f}%".
                           format(humidity),scroll_speed=0.05,
                           back_colour=[100,100,100],text_colour=
                           [0,0,255])
        sense.clear()
    print("outside of if...else statement")

main()
