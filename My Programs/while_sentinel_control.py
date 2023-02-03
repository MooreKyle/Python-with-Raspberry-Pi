#while_sentinel_control.py
from time import sleep
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    text_color = [255,0,255]
    back_color = [0,0,0]
    scroll_speed = 0.03

    h = sense.get_humidity() # priming read
    while h < 50:
        sense.show_message("Humidity = " + str(round(h,1)), \
                           scroll_speed,text_color,back_color)
        h = sense.get_humidity() # loop read
    sense.show_message("It is too humid!",scroll_speed)
main()
