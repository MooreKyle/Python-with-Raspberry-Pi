#quiz_control_robot.py
from time import sleep
from adafruit_crickit import crickit


stop = 0.0

motor_1 = crickit.dc_motor_1 # right motor
motor_2 = crickit.dc_motor_2 # left motor
motor_1.throttle = stop # right motor stopped
motor_2.throttle = stop # left motor stopped
sleep(1)


def move_forward(time:float,speed:float):
    motor_1.throttle = speed # right motor half speed forward
    motor_2.throttle = speed # left motor half speed forward
    sleep(time)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(1)

def curve_right(time:float,speed:float):
    motor_1.throttle = speed # right motor half speed forward
    motor_2.throttle = stop # left motor stopped
    sleep(2)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(1)

def curve_left(time:float,speed:float):
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = speed # left motor half speed forward
    sleep(2)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(1)
    
def move_backward(time:float,speed:float):
    motor_1.throttle = -0.5 # right motor backward
    motor_2.throttle = -0.5 # left motor backward
    sleep(2)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(1)

def rotate_right(time:float,speed:float):
    motor_1.throttle = speed # right motor half speed forward
    motor_2.throttle = -0.5 # left motor stopped
    sleep(2)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(1)

def rotate_left(time:float,speed:float):
    motor_1.throttle = -0.5 # right motor stopped
    motor_2.throttle = speed # left motor half speed forward
    sleep(2)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(1)

#DO NOT LET RED MALE-MALE TOUCH BLACK MALE-MALE WHILE CONNECTED TO RPi!
