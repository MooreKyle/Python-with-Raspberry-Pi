#for_loops.py
from sense_hat import SenseHat
from time import sleep
def main():
    sense = SenseHat()
    for i in range(11): # 0 to 10
        sense.show_message(str(i),0.03)
    for i in range(0,11,2): # 0 to 10 in steps of 2
        sense.show_message(str(i),0.03)
    for i in range(10,-1,-2): # 10 to 0 in steps of -2
        sense.show_message(str(i),0.03)
    for count in range(9,-1,-1): #9 to 0 in steps of -1
        sense.show_letter(chr(48+count),[0,255,0],[255,255,0])
        sleep(0.5)
    sense.clear()
    comedy_list = ["Moe","Larry","Curly"]
    for c in comedy_list:
        print(c)
main()
