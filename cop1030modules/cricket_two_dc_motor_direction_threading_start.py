#cricket_two_dc_motor_direction_threading.py
#Copyright (c) 2019 by Elizabeth I. Horvath
import threading
import time
from adafruit_crickit import crickit
import pygame
from pygame.locals import *

class move_robot_thread(threading.Thread):
    right = False
    left = False
    forward = False
    reverse = False
    stop_robot = False

    def __init__(self, threadID, name, rr1, rr2):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.rr1 = rr1
        self.rr2 = rr2

    def turn_right(self):
        self.right = True
        self.left = False
        self.forward = False
        self.reverse = False

    def turn_left(self):
        self.right = False
        self.left = True
        self.forward = False
        self.reverse = False

    def turn_forward(self):
        self.right = False
        self.left = False
        self.forward = True
        self.reverse = False

    def turn_reverse(self):
        self.right = False
        self.left = False
        self.forward = False
        self.reverse = True

    def stop_running(self):
        self.right = False
        self.left = False
        self.forward = False
        self.reverse = False
        self.stop_robot = True

    def pause_running(self):
        self.right = False
        self.left = False
        self.forward = False
        self.reverse = False

    def run(self):
        while True:
            if self.right == True:
                print("\nright")
                self.rr2.control_direction("pause") #switched line 64 and 65 for compatibility purposes
                self.rr1.control_direction("forward")
                time.sleep(0.5)
            elif self.left == True:
                print("\nleft")
                self.rr2.control_direction("forward") #switched line 69 and 70 for compatibility purposes
                self.rr1.control_direction("pause")
                time.sleep(0.5)
            elif self.forward == True:
                print("\nforward")
                self.rr1.control_direction("forward")
                self.rr2.control_direction("forward")
                time.sleep(0.5)
            elif self.reverse == True:
                print("\nreverse")
                self.rr1.control_direction("reverse")
                self.rr2.control_direction("reverse")
                time.sleep(0.5)
            elif self.stop_robot == False:
                print("\npause the robot")
                self.rr1.control_direction("pause")
                self.rr2.control_direction("pause")
                time.sleep(0.5)
            elif self.stop_robot == True:
                print("\nstop the robot; robot thread exits")
                self.rr1.control_direction("stop")
                self.rr2.control_direction("stop")
                time.sleep(0.5)
                return
            
class determine_direction_thread(threading.Thread):
        threadRef = threading.Thread
        rr = None

        def __init__(self,threadID,name,threadParam,rr1,rr2):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.threadRef = threadParam
            self.name = name
            self.rr1 = rr1
            self.rr2 = rr2
            pygame.init()
            pygame.display.set_mode((1,1))

        def run(self):
             while True:
                   for event in pygame.event.get():
                       if event.type == KEYDOWN:
                           print("event.key = " + str(event.key))
                           if event.key == pygame.K_DOWN:
                                self.threadRef.turn_reverse()
                           elif event.key == pygame.K_UP:
                                self.threadRef.turn_forward()
                           elif event.key == pygame.K_RIGHT:
                                self.threadRef.turn_right()
                           elif event.key == pygame.K_LEFT:
                                self.threadRef.turn_left()
                           elif event.key == 112: # 112 = p
                                self.threadRef.pause_running()
                                self.rr1.control_direction("pause")
                                self.rr2.control_direction("pause")
                                time.sleep(0.3) # wait for the motors to stop
                           elif event.key == 113: # 113 = q
                                self.threadRef.stop_running()
                                self.rr1.control_direction("stop")
                                self.rr2.control_direction("stop")
                                time.sleep(0.6) # wait for the motors to stop
                                pygame.quit()
                                return
                   time.sleep(0.2)

def main():

    motor_1 = crickit.dc_motor_1
    motor_2 = crickit.dc_motor_2

    print("press keys; up arrow, down arrow, left arrow, right arrow, p and q")
    move_robot_t1 = move_robot_thread(1,"Thread-move", \
                                      motor_1,motor_2)

    direction_t1 = determine_direction_thread(1,\
                                     "Thread-direction", move_robot_t1,\
                                              motor_1,motor_2)

    threads_list = []
    move_robot_t1.start()
    direction_t1.start()
    motor_1.start()
    motor_2.start()
    threads_list.append(move_robot_t1)
    threads_list.append(direction_t1)
    threads_list.append(motor_1)
    threads_list.append(motor_2)
    for t in threads_list:
        t.join()

main()
