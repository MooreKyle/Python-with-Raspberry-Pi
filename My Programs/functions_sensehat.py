#functions_sensehat.py
from sense_hat import SenseHat

def space_heroes_dawg(s,msg:str)->None: # s and msg are parameters # The return type being none here is like a "void" function
    s.show_message(msg,0.05)
    # msg is str data
    # None is returned

def compute_bill(number_sold:int,price_each:float)->float:
    total = number_sold * price_each
    return total

def main():
    sense = SenseHat()
    space_heroes_dawg(sense,"Captain Buck Rogers") #arguments
    space_heroes_dawg(sense,"Colonel Wilma Dearing")
    result = compute_bill(10,9.95)
    space_heroes(sense,str(result))
    sense.clear

main()
