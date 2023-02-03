#ldr_buzzer_sms.py
from gpiozero import LightSensor,PWMOutputDevice
from time import sleep
from twilio.rest import Client
def main():
    try:
        ACCOUNT_SID = "ACc4bd1f9456a4141eeb0ffc6c1223ac34" # From Twilio Account
        AUTH_TOKEN = "66038659208469c10914e4c6dd4a2a44" # From Twilio Account
        client = Client(ACCOUNT_SID,AUTH_TOKEN)
        to_phone_number = "+15615430987" # your cell phone number
        from_phone_number = "+15614258223" # phone number
        ldr_pin = 4 # GPIO 4
        ldr = LightSensor(ldr_pin)
        buzzer_pin = 17 # GPIO 17
        buzzer = PWMOutputDevice(buzzer_pin,initial_value=0.0, frequency = 2000) # Change to modify sound
        sleep(1)
        message_sent = False
        while True:
            print("ldr.value = " + str(ldr.value))
            if ldr.value < 0.9:
                print("Light Blocked")
                if not message_sent:
                    body_message = "Intruder detected"
                    client.messages.create(to=to_phone_number,from_=from_phone_number,body=body_message)
                    message_sent = True
                buzzer.pulse()
                sleep(5)
                buzzer.off()
            else:
                print("Light Not Blocked")
            sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(e)
    finally:
        ldr.close()
        buzzer.close()
main()
