#circle_class_one.py
from math import pi

class Circle():
    radius = 0

    def find_area():
        area = pi * Circle.radius ** 2
        return area

def main():
    Circle.radius = 5
    print(Circle.radius)
    print(Circle.find_area()) #Class Variable - Only 1 copy of this in memory

main()
