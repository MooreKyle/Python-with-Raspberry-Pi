#while_sentinel_control.py
from time import sleep
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    text_color = [255,0,255]
    back_color = [0,0,0]
    scroll_speed = 0.03
    slow_scroll_speed = 0.5
    text_color_2 = [0,0,255]
    h = sense.get_humidity() # priming read
    count = 1
    max_count = 20
    while h < 50 and count <= max_count:
        sense.show_message("Humidity = " + str(round(h,1)), \
                           scroll_speed,text_color,back_color)
        h = sense.get_humidity() # loop read
        count = count + 1
    if h >= 50:
        sense.show_message("It is too humid!",scroll_speed)
    if count > max_count:
        sense.show_message("We measured the humidity enough!",slow_scroll_speed,text_color_2)
main()
