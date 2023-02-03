#blink_led.py
import RPi.GPIO as GPIO
from time import sleep
import smtplib
from email.mime.text import MIMEText
def blink_delay(led_pin,delay_time,upper_limit):
    for i in range(0,upper_limit):
        GPIO.output(led_pin,True)
        sleep(delay_time)
        GPIO.output(led_pin,False)
        sleep(delay_time)
def send_email(from_address,to_address,user_name, \
               user_password,msg_text):
    msg = MIMEText(msg_text)
    msg['Subject'] = "Python with Raspberry Pi"
    msg['From'] = from_address
    msg['To'] = to_address
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(user_name,user_password)
    server.send_message(msg)
    server.quit()
def main():
    GPIO.setmode(GPIO.BCM)
    led_pin = 22 #GPIO 22
    GPIO.setup(led_pin,GPIO.OUT)
    pir_pin = 17 #GPIO 17
    GPIO.setup(pir_pin,GPIO.IN)
    email_sent = False
    try:
        while True:
            if GPIO.input(pir_pin) == 1:
                print("motion detected")
                blink_delay(led_pin,0.25,3)
                if email_sent != True:
                    send_email("youremailaddress@gmail.com", \
                      "youremailaddress@gmail.com", \
                      "youremailaddress@gmail.com","secret", \
                      "Raspberry Pi Intruder Detected!")
                    # gmail allow less secure apps
                    email_sent = True
                #blink_delay(led_pin,0.5,3)
            else:
                print("no motion detected")
            sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()

main()
