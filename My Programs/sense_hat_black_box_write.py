#sense_hat_black_box_write.py
from sense_hat import SenseHat
from time import sleep,ctime

def main():
    filename = input("Enter a filename")
    file_opened = False
    sense = SenseHat()
    try:
        sense_file = open(filename,"w")
        # "w" create a new file, delete the contents of the file, if it exists
        file_opened = True
        print("file opened")
        print("Move the pi around")
        while True:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration["x"]
            y = acceleration["y"]
            z = acceleration["z"]
            x = round(x,4)
            y = round(y,4)
            z = round(z,4)
            t1 = ctime() # human readable time
            print("{0},{1},{2},{3}".format(x,y,z,t1))
            print("{0},{1},{2},{3}".format(x,y,z,t1),file = sense_file)
            sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
    except IsADirectoryError:
        print(filename + " is a directory")
    except PermissionError:
        print("permission error, cannot open file")
    except FileNotFoundError:
        print(filename + " file cannot be opened")
    finally:
        sense.clear()
        if file_opened:
            sense_file.close()

main()
