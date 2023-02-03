#use_comp_calc.py
import sys
sys.path.append("/home/pi/cop1030modules")
from many_fun import *
from comp_calc import commission_calc
from fieldmodules.field import electric_field,magnetic_field

def main():
    comm = commission_calc(850,15)
    print(comm)
    print(commission_calc.__annotations__)
    print(commission_calc.__doc__)
    help(commission_calc)
    comp_name = input("Enter a computer name")
    print(computer_price.__annotations__)
    cost = computer_price(comp_name)
    print(cost)
    print(compute_area.__annotations__)
    print(compute_area.__doc__)
    my_side = int(input("Enter the side "))
    my_area = compute_area(my_side)
    print_area(my_area)

main()
