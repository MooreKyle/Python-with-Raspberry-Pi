#read_component_file.py

def main():
    filename = input("Enter a filename")
    file_opened = False
    try:
        comp_file = open(filename,"r")
        # "r" read only mode
        file_opened = True
        print("file opened")
        #print(type(comp_file))
        for line in comp_file:
            line = line.strip()
            print(line)
    except IsADirectoryError:
        print(filename + " is a directory")
    except PermissionError:
        print("permission error, cannot open file")
    except FileNotFoundError:
        print(filename + " file cannot be opened")
    finally:
        if file_opened:
            comp_file.close()
            print("file closed")

main()
