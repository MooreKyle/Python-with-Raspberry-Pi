#Quiz_Eight - Read Files
#Kyle Moore - 6-25-19



def main():
    filename = input("Enter a filename")
    file_opened = False
    try:
        sensehat_data_file = open(filename,"r")
        file_opened = True
        print("file opened")
        total_cost = 0
        for line in sensehat_data_file:
            line = line.strip()
            fields = line.split(",")
            cost = int(fields[1])*float(fields[2])
            print("{0:s} costs {1:.2f}".format(fields[0],cost))
            total_cost += cost
            #print(line)
        print("total cost {0:.2f}".format(total_cost))
    except IsADirectoryError:
        print(filename + " is a directory")
    except PermissionError:
        print("permission error, cannot open file")
    except FileNotFoundError:
        print(filename + " file cannot be opened")
    finally:
        if file_opened:
            sensehat_data_file.close()

main()
