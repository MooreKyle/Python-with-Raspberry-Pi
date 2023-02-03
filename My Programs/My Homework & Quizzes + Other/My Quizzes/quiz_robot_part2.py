#quiz_robot_part2.py

#libraries
from time import sleep
from adafruit_crickit import crickit

#main
def main():
    
    #Declarations
    stop = 0.0
    i = 0

    #loop "N" robot path x10
    for i in range(0,10):
        #Halted from start
        motor_1 = crickit.dc_motor_1 # right motor
        motor_2 = crickit.dc_motor_2 # left motor
        motor_1.throttle = stop # right motor stopped
        motor_2.throttle = stop # left motor stopped
        sleep(1)

        #Move forward - straight line 1
        motor_1.throttle = 0.5 # right motor half speed forward
        motor_2.throttle = 0.5 # left motor half speed forward
        sleep(2)
        motor_1.throttle = stop # right motor stopped
        motor_2.throttle = stop # left motor stopped
        sleep(1)

        #Turn right
        motor_1.throttle = 0.5 # right motor half speed forward
        motor_2.throttle = stop # left motor stopped
        sleep(2)
        motor_1.throttle = stop # right motor stopped
        motor_2.throttle = stop # left motor stopped
        sleep(1)

        #Move forward - diagonal line
        motor_1.throttle = 0.5 # right motor half speed forward
        motor_2.throttle = 0.5 # left motor half speed forward
        sleep(2)
        motor_1.throttle = stop # right motor stopped
        motor_2.throttle = stop # left motor stopped
        sleep(1)

        #Turn left
        motor_1.throttle = stop # right motor stopped
        motor_2.throttle = 0.5 # left motor half speed forward
        sleep(2)
        motor_1.throttle = stop # right motor stopped
        motor_2.throttle = stop # left motor stopped
        sleep(1)

        #Move forward - straight line 2
        motor_1.throttle = 0.5 # right motor half speed forward
        motor_2.throttle = 0.5 # left motor half speed forward
        sleep(2)
        motor_1.throttle = stop # right motor stopped
        motor_2.throttle = stop # left motor stopped
        sleep(1)

main()
