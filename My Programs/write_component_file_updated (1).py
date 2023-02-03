#write_component_file_updated.py
def main():
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
            print("{0},{1},{2}".format(component,number_ordered,price),
                                       file=comp_file)
            component = input("Enter a component, exit to quit ")
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
