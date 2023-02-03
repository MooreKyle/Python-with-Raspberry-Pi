#while_count_control.py
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    try:
        upper_limit = int(input("Enter the upper limit"))
    except ValueError:
        print("Invalid input, setting upper_limit to 10")
        upper_limit = 10
    msg = "Raspberry Pi"
    count = 1
    while count <= upper_limit:
        sense.show_message(msg,0.03,[255,0,255])
        count += 1
    msg2 = "Python"
    for count in range(1,upper_limit+1):
        sense.show_message(msg2,0.03,[0,0,255])
    sense.clear()

main()
