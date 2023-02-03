#pir_send_email.py

from picamera import PiCamera
from time import sleep
from email_graphic import send_image
import RPi.GPIO as GPIO

def main():
    camera = None
    try:
        camera = PiCamera()
        camera.rotation = 0
        camera.resolution = (1920,1080)
        camera.framerate = 15
        sleep(4)
        GPIO.setmode(GPIO.BCM)
        pir_pin = 17 # GPIO 17
        GPIO.setup(pir_pin,GPIO.IN)
        image_path = "/home/pi/Desktop/image1.jpg"
        while True:
            if GPIO.input(pir_pin) == 1:
                print("motion")
                camera.capture(image_path)
                send_image("eihorvath@gmail.com","secret", 
                           "eihorvath@gmail.com","eihorvath@gmail.com",
                           "Image of visitor","Image of visitor",image_path)
                print("email sent")
                sleep(10)
                break
            else:
                print("no motion")
            sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as message:
        print("Exiting " + str(message))
    finally:
        if camera is not None:
            camera.close()
        GPIO.cleanup()
main()
