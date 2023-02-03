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

    days_list = ["Monday","Tuesday","Wednesday",\
                 "Thursday","Friday"]
    total_hours = 0
    for empid in range(1,4):
        print("Enter the hours for employee " + str(empid))
        emp_hours = 0
        for i in range(len(days_list)):
            print(days_list[i])
            hours = int(input("Enter hours "))
            emp_hours += hours
        total_hours += emp_hours
        print(str(empid) + " worked " + str(emp_hours) +\
              " hours")
    print("total hours worked {:.2f}".format(total_hours))

main()
