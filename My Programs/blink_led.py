#blink_led.py
import RPi.GPIO as GPIO
from time import sleep

def main():
    GPIO.setmode(GPIO.BCM)
    led_pin = 22 #GPIO 22
    GPIO.setup(led_pin,GPIO.OUT)
    for i in range(1,6): #Number of times it will blink in 1 second (ie: range(1,60) will make it blink 60 times in a second)
        GPIO.output(led_pin,True)
        sleep(0.5)
        GPIO.output(led_pin,False)
        sleep(0.5)
    GPIO.cleanup() #VERY IMPORTANT

main()
