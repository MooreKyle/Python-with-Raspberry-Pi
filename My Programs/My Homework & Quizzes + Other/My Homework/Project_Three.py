#Project_Three
#Kyle Moore - 5-30-19

#libraries
from time import sleep
from sense_hat import SenseHat
from random import randint



#main
def main():
    
    #Infinite while loop in try-except statement
    evil_kid = True
    try:
        while evil_kid == True:
            print("I will not write on the board ")
    except KeyboardInterrupt: #Gracefully handle termination of infinite loop with Ctrl+c
        print("\nExiting... \n\n")
        sleep(3)

    #1st while loop - iterates from 1 to 10 & prints each iteration #
    print("\n\n*****This is the first while loop!***** ")

    i = 1
    while i <= 10:
        print("This is iteration #", i)
        sleep(0.5)
        i += 1 # i=i+1

    #2nd while loop - iterates to 20
    print("\n\n*****This is the second while loop!***** ")

    a = 0
    counter = 2
    while a <= 20:
        print("This is iteration #",counter,". The new value is:",a)
        sleep(0.5)
        counter +=1 # counter=counter+1
        a += 2 # a=a+1

    #3rd while loop
    print("\n\n*****This is the third while loop!***** ")
    
    limit = 30
    i = 0

    print("The current iteration number is",limit)
    step = int(input("\nPlease enter a negative quantity to constantly decrement by from the iteration number to 0: "))

    while limit >= 0:
        i += 1 #i=i+1
        limit=limit+step

        if limit < 0: #Handles any uneven difference
            print("Your input value subtracted from the current iteration value is", limit, "which is less than 0, & doesn't subtract evenly. Thus, the new value will be set to zero. ")
            limit = 0
            sleep(3)
            print("This is iteration #",i,". The new value is:",limit)
            break

        if limit == 0:
            print("This is iteration #",i,". The new value is:",limit)
            sleep(0.5)
            break
            
        print("This is iteration #",i,". The new value is:",limit)
        sleep(0.5)


    #1st for loop
    print("\n\n*****This is the first for loop!***** ")
    
    limit = 30
    i = 0

    print("The current iteration number is",limit)
    step = int(input("\nPlease enter a negative quantity to constantly decrement by from the iteration number to 0: "))

    for limit in range(30, -1, step):
        print("This is iteration #",i,". The new value is:",limit)
        i += 1
        sleep(0.5)


    #Random Number Game
    sense = SenseHat()
    num = randint(1,8)

    guess = int(input("\n\nHello user, please guess my number from 1 to 8: "))

    while guess != num:
        print("Please check your Sense HAT for the result...")
        sleep(1)
        sense.show_message("Nope, try again!",scroll_speed=0.03,text_colour=[255,0,0])
        guess = int(input("\nTry guessing another number from 1 to 8: "))

        if guess == num:
            print("Please check your Sense HAT for the result...")
            sleep(1)
            sense.show_message("You WIN!",scroll_speed=0.03,text_colour=[0,255,0])
            break


    #2nd for loop
    print("\n\n*****This is the second for loop!***** ")
    
    limit = 3
    i = 0
    step = 5

    print("The current iteration number is",limit,"and the incrementation value is",step)

    for limit in range(3, 99, step):
        print("This is iteration #",i,". The new value is:",limit)
        i += 1
        sleep(0.5)


    #4th while loop
    print("\n\n*****This is the fourth while loop!***** ")
    
    limit = 3
    i = 0

    print("The current iteration number is",limit,"and the incrementation value is",step)

    while limit < 98:
        i += 1 #i=i+1
        limit=limit+step
            
        print("This is iteration #",i,". The new value is:",limit)
        sleep(0.5)


    #nested for loops
    print("\n\n*****This is a nested for loops structure!***** ")
    
    for i in range(0, 3, 1):
        for a in range(10, 0, -1):
            print("i = " + str(i) + ",     a = " + str(a))


    #Grocery Store Application
    print("\n\n*****This is the Grocery Store Application!***** ")

    quantity = 1 #priming read for quantity
    cost = 0
    SALES_TAX = .35
    subtotal = 0

    while quantity >= 1:
        quantity = int(input("\nPlease enter the quantity of items: "))

        if quantity <= 0:
            print("Invalid Quantity! Quitting...")
            sleep(3)
            break
        
        name = str(input("\nPlease enter the name of the item: "))
        price = float(input("\nPlease enter the price of the item: "))

        cost = quantity * price
        subtotal = subtotal + cost

        print("\n\nName:",name,"\t\tCost: $" + format(cost,"7.2f"))

    SALES_TAX = float(input("\nPlease enter the sales tax rate: "))
    tax_total = subtotal * SALES_TAX
    total = subtotal + (subtotal * SALES_TAX)

    print("Total: $" + format(total,"7.2f"))


    #Piezo Buzzer - Beep buzzer x5 with a for loop
        
    
                      
main() #Call main

