#use_comp_calc.py
from comp_calc import commission_calc

def main():
    comm = commission_calc(850,15)
    print(comm)
    print(commission_calc.__annotations__)
    print(commission_calc.__doc__)
    help(commission_calc)

main()
