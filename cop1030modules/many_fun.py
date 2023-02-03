#many_fun.py
def computer_price(name_computer:str)->float:
    price = 700.0
    if name_computer.lower() == "Dell".lower():
        price = 600.0
    elif name_computer.lower() == "Raspberry Pi".lower():
        price = 35.00
    elif name_computer.lower() == "Macintosh".lower():
        price = 2560.00
    return price

def compute_area(side:int)->int:
    """
    This function computes the area of a square
    """
    area = side ** 2
    return area

def print_area(area:float)->None:
    print("The area is {0:3d}".format(area))
    
