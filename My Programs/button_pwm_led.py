#button_pwm_led.py

import RPi.GPIO as GPIO
from time import sleep

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)

    pwm_green = GPIO.PWM(18,100) # GPIO 18 permission 1/100Hz
    pwm_green.start(0) # duty cycle is 0, LED is off
    GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    # GPIO 04 is pulled high by default
    # when the button is pressed, GPIO 04 is pulled
    # down to ground
    try:
        while True:
            if GPIO.input(4) == 0:
                print("button pressed")
                for value in range(0,101,5):
                    pwm_green.ChangeDutyCycle(value)
                    # duty cycle is 100 is fully on
                    sleep(0.3)
                for value in range(100,-1,5):
                    pwm_green.ChangeDutyCycle(value)
                    sleep(0.3)
            else:
                print("button not pressed")
                sleep(0.3)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        pwm_green.stop()
        GPIO.cleanup()

main()
