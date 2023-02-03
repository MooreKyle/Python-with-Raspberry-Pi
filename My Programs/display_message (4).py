#display_message.py
from sense_hat import SenseHat

def main():     #create a function
    print("Welcome to Python with Raspberry Pi")
    name = input("Enter your name ")
    print("Hello " + name)
    count = int(input("How many people are in the class? "))
    sense = SenseHat()
    temperature = sense.get_temperature()
    fahr = 9/5 * temperature + 32
    msg = "The temperature is " + format(fahr,"5.2f")
    sense.show_message(msg,scroll_speed=0.1,back_colour=[0,0,255],text_colour=[255,255,0])
    sense.clear()
    print("Your name is\"" + format(name,"20s") + "\"")
    print("There are\"" + format(count,"10d") + "\" students in the class")
    print("Your name is\"" + format(name,">20s") + "\"")
    print("There are\"" + format(count,"<10d") + "\" students in the class")
main()          #call the main function
