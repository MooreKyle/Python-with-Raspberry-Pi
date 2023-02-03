#threads_one.py

import threading
import time

class myThread(threading.Thread):
    def __init__(self,thread_id,name,counter,delay):
        threading.Thread.__init__(self)
        self.name = name
        self.threadID = thread_id
        self.count = counter
        self.delay = delay
    def run(self):
        print("Starting " + self.name)
        self.print_time()
        print("End of run " + self.name)
    def print_time(self):
        while self.count > 0:
            time.sleep(self.delay)
            print("{:s} {:d}".format(time.ctime(),self.threadID))
            self.count -= 1

def main():
    thread1 = myThread(1,"Thread One", 10, 1)
    thread2 = myThread(2,"Thread Two", 10, 2)
    thread3 = myThread(3,"Thread Three", 10, 3)
    thread1.start()
    thread2.start()
    thread3.start()
    thread_list = []
    thread_list.append(thread1)
    thread_list.append(thread2)
    thread_list.append(thread3)
    for t in thread_list:
        t.join() # wait until all threads end
    print("End of main")

main()
