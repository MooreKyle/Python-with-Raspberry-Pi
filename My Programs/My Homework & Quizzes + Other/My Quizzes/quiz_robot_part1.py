#quiz_robot_part1

from time import sleep
from adafruit_crickit import crickit



def main():

    stop = 0.0

    motor_1 = crickit.dc_motor_1 # right motor
    motor_2 = crickit.dc_motor_2 # left motor
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(1)
    
    #Reverse for 1 second & stop for 2 seconds
    motor_1.throttle = -0.5 # right motor backward
    motor_2.throttle = -0.5 # left motor backward
    sleep(1)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped

    #sleep for 2 seconds and turn left (90 degrees)
    sleep(2)
    motor_1.throttle = 0.75
    motor_2.throttle = 0.5
    sleep(1)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(2)

    #Forward for 2 seconds & stop
    motor_1.throttle = 0.75
    motor_2.throttle = 0.5
    sleep(2)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped

main()
