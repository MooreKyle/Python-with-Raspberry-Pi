#ldr_buzzer_sms.py
from gpiozero import LightSensor,PWMOutputDevice
from time import sleep

def main():
    try:
        ldr_pin = 4 # GPIO 4
        ldr = LightSensor(ldr_pin)
        buzzer_pin = 17 # GPIO 17
        buzzer = PWMOutputDevice(buzzer_pin,initial_value=0.0, frequency = 2000) # Change to modify sound
        sleep(1)
        while True:
            print("ldr.value = " + str(ldr.value))
            if ldr.value < 0.9:
                print("Light Blocked")
                buzzer.pulse()
                sleep(5)
                buzzer.off()
            else:
                print("Light Not Blocked")
            sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ldr.close()
        buzzer.close()
main()
