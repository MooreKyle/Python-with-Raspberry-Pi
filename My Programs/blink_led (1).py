#blink_led.py
import RPi.GPIO as GPIO
from time import sleep

def blink_delay(led_pin,delay_time,upper_limit):
    for i in range(0,upper_limit):
        GPIO.output(led_pin,True)
        sleep(delay_time)
        GPIO.output(led_pin,False)
        sleep(delay_time)

def main():
    GPIO.setmode(GPIO.BCM)
    led_pin = 22 #GPIO 22
    GPIO.setup(led_pin,GPIO.OUT)
    blink_delay(led_pin,0.25,10)
    GPIO.cleanup()

main()
