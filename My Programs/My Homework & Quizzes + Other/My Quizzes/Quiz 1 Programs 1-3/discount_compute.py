#discount_compute.py
#Kyle Moore - 5-29-19



def main():

    #Get cost and user_code from user
    cost = float(input("Please enter the cost: "))
    user_code = str(input("Please enter the user code: "))

    #Decision Structure - compute discount based on user input
    if user_code == "A":
        discount = 0.08 * cost
    elif user_code == "B":
        discount = 0.10 * cost
    elif user_code == "C":
        discount = 0.05 * cost
    elif user_code == "D" or user_code == "E":
        discount = 0.035 * cost
    else:
        discount = 0.02 * cost

    #Compute total_bill
    total_bill = cost - discount
    print("The total bill is: total_bill",format(total_bill,".2f"))

main()
