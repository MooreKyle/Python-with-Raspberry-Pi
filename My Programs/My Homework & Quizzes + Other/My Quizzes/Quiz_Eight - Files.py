#Quiz_Eight - Files
#Kyle Moore - 6-25-19



def main():
    filename = input("Enter a filename")
    file_opened = False
    try:
        sensehat_data_file = open(filename,"r")
        # "r" read only mode
        file_opened = True
        print("file opened")
        #print(type(comp_file))
        total_cost = 0
        for line in comp_file:
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
            comp_file.close()



    filename = input("Enter a filename")
    file_opened = False
    try:
        comp_file = open(filename,"w")
        # "a" append creates if it does not exist, adds to the end of the file
        # "w" create a new file, delete the contents of the file, if it exists
        file_opened = True
        print("file opened")
        component = input("Enter a component ")
        while component != "exit":
            number_ordered = input("Number Ordered? ")
            price = input("Price? ")
            print("{0},{1},{2}".format(component,number_ordered
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
