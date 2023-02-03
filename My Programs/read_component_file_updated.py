#read_component_file_updated.py
def main():
    filename = input("Enter a filename")
    file_opened = False
    try:
        comp_file = open(filename,"r")
        # "r" read only mode
        file_opened = True
        print("file opened")
        #print(type(comp_file))
        total_order_cost = 0
        for line in comp_file:
            line = line.strip()
            fields = line.split(",")
            cost = int(fields[1])*float(fields[2])
            print("{0:s} costs {1:.2f}".format(fields[0],cost))
            total_order_cost += cost
            #print(line)
        print("total cost {0:.2f}".format(total_order_cost))
    except IsADirectoryError:
        print(filename + " is a directory")
    except PermissionError:
        print("permission error, cannot open file")
    except FileNotFoundError:
        print(filename + " file cannot be opened")
    finally:
        if file_opened:
            comp_file.close()

main()
