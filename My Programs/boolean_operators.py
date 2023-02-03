#boolean_operators.py
from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    t = sense.get_temperature()
    h = sense.get_humidity()
    p = sense.get_pressure()

    t = round(t,2)
    h = round(h,2)
    p = round(p,2)

    if(p < 950) and (t > 30):
        sense.show_message("Hot with a storm warning",0.05)

    if not(p >= 950):
        sense.show_message("Storm warning",text_colour=[0,0,255],
                           scroll_speed=0.05)

    if(t > 20) and (h >= 40):
        sense.show_message("It is hot and humid",0.08,[255,0,0],
                           [255,255,0])
        answer = input("Do you want to see the temperature and humidity? ").lower()
        if answer == "y":
            sense.show_message("temperature = {0:2f}C humidity = {1:.2f}%".
                               format(t,h))
        else:
            sense.show_message("Maybe you want to see the pressure {0:.0f}".
                        format(p))

    sense.clear()
main()
