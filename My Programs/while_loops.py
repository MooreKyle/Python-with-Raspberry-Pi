#while_loops.py
def main():
    try:
        age = int(input("Enter your age "))
        while age < 0 or age >= 150: # sentinel control
            age = int(input("Enter your age. " + 
                        "Age must be greater than or equal to 0 or " +
                        " less than 150"))
        print("Valid age is {0:2d}".format(age))

        day = 0
        total_miles = 0.0
        miles = 1
#     miles = float(input("Enter the number of miles driven ")) # priming read
        while miles > 0:  # sentinel control
            try:
                miles = float(input("Enter the number of miles driven ")) # loop read
                total_miles = total_miles + miles
                day += 1
            except ValueError:
                print("Invalid input")
        print(total_miles)
        if day >= 1:
            average_miles = total_miles / day
            print(average_miles)
    except ValueError:
        print("non-numeric value input")
   
main()
