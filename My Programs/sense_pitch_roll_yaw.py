#sense_pitch_roll_yaw.py

from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    or_label = ["pitch","roll","yaw"]
    or_data = [[0]*10,[0]*10,[0]*10]
    count = 0
    while count <= 9:
        orientation = sense.get_orientation()
        or_data[0][count] = orientation["pitch"]
        or_data[1][count] = orientation["roll"]
        or_data[2][count] = orientation["yaw"]
        print("sample number " + str(count))
        sleep(1)
        count = count + 1
    count = 0
    while count <= 2:
        count2 = 0
        print(or_label[count])
        while count2 <= 9:
            print(format(or_data[count][count2],".4f"))
            count2 += 1
        print()
        count += 1
    sense.clear()
main()
