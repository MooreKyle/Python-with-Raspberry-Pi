#sense_hat_list.py
from sense_hat import SenseHat
from time import sleep
def main():
    sense = SenseHat()
    temp_list = []
    try:
        while True:
            temperature = sense.get_temperature()
            temp_list.append(temperature)
            print("temperatures recorded " + str(len(temp_list)))
            sleep(0.5)
    except KeyboardInterrupt:
        sense.clear()
    for i in range(len(temp_list)):
        sense.show_message(format(temp_list[i],".2f"),scroll_speed=0.05)
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    sense.show_message("maximum " + format(max_temp,".2f"),scroll_speed=0.03)
    sense.show_message("minimum " + format(min_temp,".2f"),scroll_speed=0.03)
    sense.clear()
main()
