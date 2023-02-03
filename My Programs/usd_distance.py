#usd_detector.py
import RPi.GPIO as GPIO
from time import sleep,time
from pygame import mixer

TRIGGER_PIN = 26
ECHO_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
sleep(2)
# Simon Monk's Code
def send_trigger_pulse():
    GPIO.output(TRIGGER_PIN, True)
    sleep(0.001)
    GPIO.output(TRIGGER_PIN, False)
def wait_for_echo(value,timeout):
    count = timeout
    while GPIO.input(ECHO_PIN) != value and count > 0:
        count = count - 1
def get_distance():
    send_trigger_pulse()
    wait_for_echo(True,10000)
    start = time()
    wait_for_echo(False,10000)
    finish = time()
    pulse_len = finish - start
    distance_cm = pulse_len * 343 * 100 / 2
    return distance_cm
def play_sound():
    mixer.init()
    mixer.music.load("car_door.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        sleep(0.01)
    for i in range(4):
        mixer.music.load("Dog1.wav")
        mixer.music.play()
        while mixer.music.get_busy():
            sleep(0.01)
        sleep(1)
        
def main():
    try:
        while True:
            distance = get_distance()
            print("Distance in cm " + str(distance))
            sleep(0.1)
            if distance < 30:
                play_sound()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up")
main()


    










    



    
