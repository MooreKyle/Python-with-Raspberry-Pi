#Quiz_Eight - Write Files
#Kyle Moore - 6-25-19



def main():
    filename = input("Enter a filename")
    file_opened = False
    try:
        sensehat_data_file = open(filename,"w")
        file_opened = True
        print("file opened")
        customer_name = input("Enter a customer name: ")
        while customer_name != "exit":
            number_ordered = input("Number Ordered? ")
            print("{0},{1}".format(customer_name,number_ordered),file=sensehat_data_file)
            customer_name = input(str("Please enter the customer name: "))
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
