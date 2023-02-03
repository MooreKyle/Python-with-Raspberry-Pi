#control_robot.py
from time import sleep
from adafruit_crickit import crickit

def main():
    motor_1 = crickit.dc_motor_1 # right motor
    motor_2 = crickit.dc_motor_2 # left motor

    motor_1.throttle = 0 # right motor stopped
    motor_2.throttle = 0 # left motor stopped
    sleep(1)

    motor_1.throttle = 0.5 # right motor half speed forward
    motor_2.throttle = 0.5 # left motor half speed forward
    sleep(2)

    #right turn
    motor_1.throttle = 0.0 # right motor stopped
    motor_2.throttle = 0.5 # left motor half speed forward
    sleep(2)
    motor_1.throttle = 0 # right motor stoped
    motor_2.throttle = 0 # left motor stopped
    sleep(1)

    #left turn
    motor_1.throttle = 0.5 # right motor half speed forward
    motor_2.throttle = 0.0 # left motor stopped
    sleep(2)
    motor_1.throttle = -0.5 # right motor backward
    motor_2.throttle = -0.5 # left motor backward
    motor_1.throttle = 0 # right motor stopped
    motor_2.throttle = 0 # left motor stopped
    sleep(1)

main()

#DO NOT LET RED MALE-MALE TOUCH BLACK MALE-MALE WHILE CONNECTED TO RPi!
