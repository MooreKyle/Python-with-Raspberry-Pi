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
    pir_pin = 17 #GPIO 17
    GPIO.setup(pir_pin,GPIO.IN)
    try:
        while True:
            if GPIO.input(pir_pin) == 1:
                print("motion detected")
                blink_delay(led_pin,0.25,3)
                #blink_delay(led_pin,0.5,3)
            else:
                print("no motion detected")
            sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()

main()
