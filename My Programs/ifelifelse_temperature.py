#ifelifelse_temperature.py
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    celsius = sense.get_temperature()
    temperature = 9/5*(celsius) + 32
    if temperature >= 90:
        sense.show_message("It is hot!",text_colour=[255,0,0],
                           scroll_speed=0.05)
    elif temperature >= 70:
        sense.show_message("It is pleasant",text_colour=[255,255,0],
                           scroll_speed=0.05)
    elif temperature >= 50:
        sense.show_message("It is cool",text_colour=[0,0,255],
                           scroll_speed=0.05)
    else:
        sense.show_message("It is cold",text_colour=[0,0,255],
                           scroll_speed=0.05)
    sense.show_message("temperature = {0:5.2f}".format(temperature))
    sense.clear()
main()
