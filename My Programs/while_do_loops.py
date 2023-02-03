#while_do_loops.py
from sense_hat import SenseHat

def main():
    age = int(input("Enter your age "))
    while age < 0 or age >= 150:
        age = int(input("Enter your age. " + "Age must be greater than or equal to 0 or " + " less than 150"))
    print("Valid age is {0:2d}".format(age))

    miles = float(input("Enter the number of miles driven ")) # priming read
    day = 1
    total_miles = 0.0
    while miles > 0:
        total_miles = total_miles + miles
        day += 1
        miles = float(input("Enter the number of miles driven ")) # loop read
    print(total_miles)
    if day >= 1:
        average_miles = total_miles / (day-1)
        print(average_miles

main()
