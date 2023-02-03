#conditional_homework.py
#Project Two - Kyle Moore

#Get libraries
from sense_hat import SenseHat
from time import sleep



#main body
def main():

    #**********1.Calculate area of a right triangle**********

    #Get base and height from user
    base = int(input("Please enter the base of a right triangle: "))
    height = int(input("Please enter the height of a right triangle: "))

    #Input Validation - base and height must be > 0
    if base < 0 or height < 0:
        print("Invalid data. ")

    #Calculate and print area with appropriate formatting
    area = base * height
    print("The area of the right triangle is: ",format(area,"5.2f"))
    print("The area of the right triangle is: ",format(area,"3.1e"))



    #**********2.Choice for Dinner**********

    #Display list & get answer from user
    answer = input("\n\nm. The Muay Thai Kitchen\ns. The Spaghetti Palace\nt. The Taco Guru\n\nWhere do you want to have dinner? ")

    #Decision Structure - Choice selected via answer from user
    if answer.startswith("m"):
        print("Thai food is delicious")
    elif answer.startswith("s"):
        print("Italian food is delicious")
    elif answer.startswith("t"):
        print("Mexican food is delicious")
    else: #Default
        print("But we'll starve.")



    #**********3.HILO number Sense HAT**********

    #Declaration/Initialization
    sense = SenseHat()
    sense.clear() #Fresh Start

    #try-except ValueError - Only accept numeric values for number
    try:
        #Get number & scroll_speed from user
        num = int(input("\n\nPlease enter a number between 1 and 100: "))
        scroll_speed = float(input("Please enter the scroll speed for the message(s) following (Default: 0.05): "))
    except ValueError:
        #Error Handler - Set default value for number if non-numeric/invalid
        print("Invalid value for number, setting number to 1. ")
        num = 1
        sleep(3)

    #Input Valid. & Decision - Verify if number is LO, HI, or invalid
    if num >= 1 and num <= 50:
        sense.show_message("LO",scroll_speed=0.05,text_colour=[0,0,255])
    elif num >= 51 and num <= 100:
        sense.show_message("HI",scroll_speed=0.05,text_colour=[255,0,0])
    else:
        print("Error! The value entered for number is out of bounds! ")



    #**********4.Compute tke & gpe**********

    #Declaration
    g = 9.8

    #Get m, v, and h from user
    m = float(input("Please enter the mass (m): "))
    v = float(input("Please enter the velocity (v): "))
    h = float(input("Please enter the height (h): "))

    #Input Validation - Verify m, v, & h are > 0
    if m > 0 and v > 0 and h > 0:
        #Calculate tke & gpe
        tke = 0.5 * m * v**2
        gpe = m * g * h
    else:
        print("Invalid data. ")

    #Notify user if either tke or gpe is > 100
    if tke > 100 or gpe > 100:
        print("tke or gpe is greater than 100")

    #Print tke & gpe in two different formats
    print("tke = " + format(tke, "12.3e"), "gpe = " + format(gpe, "12.3e"))
    print("tke = " + "{:10,.1f}".format(tke), "gpe = " + "{:10,.1f}".format(gpe) + "\n")

main() #Call main()
