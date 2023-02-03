#display_message.py
from sense_hat import SenseHat

def main():     #create a function
    print("Welcome to Python with Raspberry Pi")
    name = input("Enter your name ")
    print("Hello " + name)
    sense = SenseHat()
    temperature = sense.get_temperature()
    msg = "The temperature is " + str(temperature)
    sense.show_message(msg,scroll_speed=0.1,back_colour=[0,0,255]),\
              text_colour=[255,255,0])
    sense.clear()
    
main()          #call the main function
