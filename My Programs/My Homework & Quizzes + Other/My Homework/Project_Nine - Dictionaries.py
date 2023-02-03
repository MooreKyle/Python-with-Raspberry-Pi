#Project_Nine - Dictionaries
#Kyle Moore - 6-25-19

def main():
    tickets_sold_dict = {}

    user_input = "" #Priming read/placeholder initialization of conditional variable
    while user_input != "quit":
        key = input(str("Please enter a key (ie: Smart Figures,Guardians of the Universe,Rogue Eight): "))
        value = input(str("Please enter a value: (ie: 1096,2400,958): "))

        tickets_sold_dict[key] = cost #Adds new item based on user input?

        user_input = input(str("Would you like to enter another key and it's value? (Enter quit to quit): "))

    for key in tickets_sold_dict.keys():
        print(key)

    for value in tickets_sold_dict.values():
        print(value)

    total = sum(len(tickets_sold_dict.values()))
    print("The sum of the values is",total)

    movie_tickets_dict = {"Early Bird":511,"Matinee":343,"Evening":942}

    #Program is incomplete

main()
