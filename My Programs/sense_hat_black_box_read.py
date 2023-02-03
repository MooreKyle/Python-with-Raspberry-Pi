#sense_hat_black_box_read.py

def main():
    filename = input("Enter a filename")
    file_opened = False
    try:
        sense_file = open(filename,"r")
        # "r" read only mode
        file_opened = True
        print("file opened")
        for line in sense_file:
            print(line.strip())
        sense_file.seek(0) # move the file pointer back to the first character
        line = sense_file.readline()
        while line != "":
            line = line.strip()
            data_list = line.split(",") # split on the comma delimeter
            print("x = " + format(data_list[0]))
            print("y = " + format(data_list[1]))
            print("z = " + format(data_list[2]))
            print("t = " + format(data_list[3]))
            line = sense_file.readline()
    except IsADirectoryError:
        print(filename + " is a directory")
    except PermissionError:
        print("permission error, cannot open file")
    except FileNotFoundError:
        print(filename + " file cannot be opened")
    finally:
        if file_opened:
            sense_file.close()

main()
