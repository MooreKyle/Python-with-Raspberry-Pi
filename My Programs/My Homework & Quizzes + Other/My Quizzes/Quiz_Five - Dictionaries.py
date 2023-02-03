#Quiz_Five - Dictionaries
#Kyle Moore - 6-25-19



#5.
def find_sandwich_function(dictionary:dict,key,number_sold:int):
    try:
        find = input("Enter the key ")
        print(dictionary[find])
    except KeyError:
        print("The key was not found")
    find = input("Enter the key ")
    if find in dictionary:
        print(dictionary[find])
        total_price = number_sold * value
        return total_price
    else:
        print("The key was not found")
        return 0.0
    print(type(dictionary.items()))
    print(type(dictionary.keys()))



def main():
    #1. Dictionary: sandwich_dict w/ appropriately assigned values
    sandwich_dict = {"Peanut Butter & Jelly":2.50,"Hummus Wrap":3.75,"Ham & Swiss Cheese":4.50,"BLT":3.75}

    user_input = "" #Priming read/placeholder initialization of conditional variable
    #2.
    while user_input != "quit":
        sandwich = input(str("Please enter the name of the sandwich you would like: (ie: Peanut Butter & Jelly, Hummus Wrap, Ham & Swiss Cheese, BLT: "))
        cost = input(str("Please enter the cost of the sandwich: (ie: 2.50, 3.75, 4.50, 3.75): "))

        sandwich_dict[sandwich] = cost #Adds new item based on user input? How to convert to float?

        user_input = input(str("Would you like to enter another sandwich and it's cost? (Enter quit to quit): "))

    sandwich_dict["Greek Gyro"] = 3.25
    sandwich_dict["Taco"] = 3.25
    sandwich_dict["quit"] = quit

    #3. Use values function to access keys in sandwich_dict & loop to print out values
    print("\n\nvalues in sandwich_dict: ")
    for e in sandwich_dict.values():
        print(e)

    #4. Compute & print sum of all values for the sandwich
    total = sum(sandwich_dict.values())
    print("total of all components {0:.2f}".format(total))

    #6. Call function from main w/ appropriate arguments & assign returned value to a variable, total_cost, & print total_cost
    find_sandwich_function(sandwich_dict,"BLT",4)
    total_cost = total_price
    print("The total cost is: total_cost",format(total_cost,".2f"))

    #BONUS.
    fighter_dict = {Rhonda:"fighting",George:{"boxing":300000,"inventing":500000},Junior:["mma","acting"]}
    #use isinstance method to print out each value correctly on a separate line

main()
