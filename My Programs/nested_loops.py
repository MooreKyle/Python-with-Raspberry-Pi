#nested_loops.py
from sense_hat import SenseHat
from time import sleep

def main():
    for i in range(1,4):
        for j in range(0,5,2):
            print("i = " + str(i) + "j = " + str(j))

    sense = SenseHat()
    for row in range(0,8):
        for col in range(0,8):
            sense.set_pixel(row,col,[0,0,255])
            sleep(0.1)
    sleep(5)
    sense.clear()

main()
