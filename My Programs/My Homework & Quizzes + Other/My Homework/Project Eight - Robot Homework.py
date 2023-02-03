#Project Eight - Robot Homework
#Kyle Moore - 6-22-19

#libraries
from time import sleep
from adafruit_crickit import crickit

#main
def main():

    #Declarations
    stop = 0.0

    motor_1 = crickit.dc_motor_1 # right motor (Required for Robot Functionality)
    motor_2 = crickit.dc_motor_2 # left motor (Required for Robot Functionality)

    #Begin w/ Robot Stopped - Fresh Start
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(2)
    
    
    
    #Move Robot forward for 10 seconds
    motor_1.throttle = 0.6 # right motor 3/5 speed forward
    motor_2.throttle = 0.6 # left motor 3/5 speed forward
    sleep(10)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(2)
    
    #Right Turn (Quarter Turn - 45 Degrees)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = 0.6 # left motor 3/5 speed forward
    sleep(0.5)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(2)
    
    #Move Robot forward for 10 seconds (2nd Time)
    motor_1.throttle = 0.6 # right motor 3/5 speed forward
    motor_2.throttle = 0.6 # left motor 3/5 speed forward
    sleep(10)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(2)
    
    #Left Turn (Quarter Turn - 45 Degrees)
    motor_1.throttle = 0.6 # right motor 3/5 speed forward
    motor_2.throttle = stop # left motor stopped
    sleep(0.5)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(2)
    
    #Move Robot Backwards for 10 seconds
    motor_1.throttle = -0.6 # right motor 3/5 speed backwards
    motor_2.throttle = -0.6 # left motor 3/5 speed backwards
    sleep(10)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(2)
    
    #**********Have Robot Make a Path of a Rounded Rectangle**********
    
    #Move Robot forward for 5 seconds
    motor_1.throttle = 0.6 # right motor 3/5 speed forward
    motor_2.throttle = 0.6 # left motor 3/5 speed forward
    sleep(5)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(0.01)
    
    #Right Turn (U-Turn - 180 Degrees)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = 0.6 # left motor 3/5 speed forward
    sleep(1)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(0.01)
    
    #Move Robot forward for 5 seconds (2nd Time)
    motor_1.throttle = 0.6 # right motor 3/5 speed forward
    motor_2.throttle = 0.6 # left motor 3/5 speed forward
    sleep(5)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(0.01)
    
    #Right Turn (U-Turn - 180 Degrees) (2nd Time)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = 0.6 # left motor 3/5 speed forward
    sleep(1)
    motor_1.throttle = stop # right motor stopped
    motor_2.throttle = stop # left motor stopped
    sleep(0.01)
    
main()
