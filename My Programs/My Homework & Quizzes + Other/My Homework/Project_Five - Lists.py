#Project_Five - Lists
#Kyle Moore - 6-25-19

#libraries
from time import sleep
from sense_hat import SenseHat



def main():
    #Declare & Initialize List: sports_team_list
    sports_team_list = ["Dolphins","Marlins","Miami Heat","NE Patriots","NY Yankees","LA Dodgers"]

    #Print number of teams & each individual team from list
    print("There are a total of 6 teams in this sports team list!\n")
    for i in range(len(sports_team_list)):
        print(sports_team_list[i])
    print("\n")

    #Declare & Initialize list: sports_item_list & append new items with sentinel-controlled loop via user input
    sport_list = []
    try:
        item = input("Enter a sports item: ")
        while item != "exit":
            sport_list.append(item)
            item = input("Enter a sports item, or enter exit to quit: ")
        for s in sport_list:
            print(s)
    except KeyboardInterrupt: #Ctrl+c to exit
        print("Exiting... \n\n")
        sleep(3)

    #Record 25 pressure measurements & compute & display average on sense HAT
    pressure_list = []
    sense = SenseHat() 
    sense.clear() #Fresh Start

    for p in range(0,25):
        pressure = sense.get_pressure()
        pressure_list.append(pressure)
        pressure = float(pressure)
        sleep(1)
    total = sum(len(pressure_list))
    average = total / 25
    sense.show_message("The average pressure is",average,scroll_speed=0.05)

    #Create a list of lists & find sum of all elements
    list_of_lists = [[0]*4,[0]*4,[0]*4] # three rows, four columns
    for row in range(len(list_of_lists)): # number of rows
        for col in range(len(list_of_lists[row])): # number of columns
            list_of_lists[row][col] = int(input("row element" + str(row) + " col element" + str(col)))
    total = 0
    for row in range(len(list_of_lists)): # number of rows
        for col in range(len(list_of_lists[row])): # number of columns
            total += list_of_lists[row][col]
    print("the total of all elements is" + str(total))

    #Find sum of elements in a row number via user input
    row = input("Please enter a row number: ")
    for row in range(len(list_of_lists)): # number of rows
        sum_row_elements = sum(len(list_of_lists[row]))
    print("The sum of the elements in the row is",sum_row_elements)

    #Print discounted_cost w/ proper formatting for both instances of function being called & completed
    discounted_cost = compute_discount(150.78,member=True)
    print("The discounted cost is" + format(discounted_cost,'0.2f'))
    discounted_cost = compute_discount(98.23,member=False)
    print("The discounted cost is" + format(discounted_cost,'0.2f'))

main()



#Function: compute_discount - add comments & annotations
def compute_discount(cost:float,member:bool)->None:
    if member:
        mem_discount = 0.10
        print("You are a member. Thus, you will receive a 10% discount. ")
    else:
        mem_discount = 0
        print("You are not a member. So... no discount for you! Did you get the reference? But seriously, no discount. ")

    print("Today is Cyber Tuesday, so all customers will get a 5% discount. ")
    tue_discount = 0.05

    #Compute total discounted_cost & return to main
    discount = tue_discount + mem_discount
    discounted_cost = cost - (cost * discount)
    return discounted_cost
