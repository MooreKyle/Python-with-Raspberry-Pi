#quiztwo_partfour.py
#Kyle Moore - 6-5-19



#Function: shipping_cost
def shipping_cost(base_fee:float,zone:int):
    if zone >= 1 and zone <= 4:
        cost = base_fee * 2
    elif zone == 5 or zone == 6:
        cost = base_fee * 1.755 + 7.5
    elif zone == 7 or zone == 8 or zone == 9:
        cost = base_fee * 3.125 + 9.5
    else:
        cost = base_fee * 4.25

    #return cost
    return cost



#main
def main():
    base_fee = float(input("Please enter the base fee: "))
    zone = int(input("Please enter a value greater than 0 for the zone: "))

    #Call function: shipping_cost
    cost = shipping_cost(base_fee,zone)

    #Print cost w/ two decimal places of precision
    print("The cost is: " + format(cost,"0.2f"))



#def resistor_cost()

main() #call main
