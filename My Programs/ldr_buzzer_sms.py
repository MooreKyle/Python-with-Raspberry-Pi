#ldr_buzzer_sms.py
from gpiozero import LightSensor,PWMOutputDevice
from time import sleep

def main():
    try:
        ldr_pin = 4 # GPIO 4
        ldr = LightSensor(ldr_pin)
        sleep(1)
        while True:
            print("ldr.value = " + str(ldr.value))
            if ldr.value < 0.9:
                print("Light Blocked")
            else:
                print("Light Not Blocked")
            sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ldr.close()
main()
