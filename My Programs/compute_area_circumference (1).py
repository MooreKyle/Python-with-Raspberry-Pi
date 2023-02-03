#compute_area_circumference
from math import pi

def main():
    try:
        radius=int(input("Please enter the radius "))
    except ValueError:
        print("Invalid value for radius, setting radius to 0")
        radius = 0
    except KeyboardInterrupt: # Ctrl+C
        return
    if radius > 0:
        area = pi * radius ** 2 #"**" = exponential power
        circumference = 2 * pi * radius
        print("area = " + format(area,".2f")) # format function
        str_area = format(area,".2f")

    else:
        print("radius is less than or equal to 0")
        main()

main()
