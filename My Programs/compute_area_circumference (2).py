#compute_area_circumference.py
from math import pi
def main():
    try:
        radius = int(input("Please enter the radius "))
    except ValueError:
        print("Invalid value for radius, setting radius to 0")
        radius = 0
    except KeyboardInterrupt: # Ctrl+C
        return
    if radius > 0:
        area = pi * radius ** 2
        circumference = 2 * pi * radius
        print("area = " + format(area,".2f")) # format function
        str_area = format(area,".2f")
        print(str_area)
        print("circumference = {0:.3e}".format(circumference)) # format method
        print("{0:.3e} {1:.3e}".format(radius,circumference)) # format method
        print("{0:.3e} {1:.3e} {2:.3e}".format(radius,circumference,area)) # format method
    else:
        print("radius is less than or equal to 0")
        main()       
main()
