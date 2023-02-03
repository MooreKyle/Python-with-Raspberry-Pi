#circle_class_two.py
from math import pi
from random import randint

class Circle():
    count_circle = 0
    #class variable; shared amongst all Circle objects
    def __init__(self,radius=5,x=0,y=0,color="green"):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.area = 0
        self.find_area()
        Circle.count_circle += 1
        print(dir())
        print(type(self))
        print(type(Circle.count_circle))

    def find_area(self):
        test = 0 # local variable; cannot be accessed outside of the method
        self.area = pi * self.radius**2
        return self.area

    def __str__(self):
        return "radius of circle " + str(self.radius) + " x = " + \
    str(self.x) + " y = " + str(self.y) + " area = " + str(self.area) + \
    " count_circle " + str(Circle.count_circle)

def main():
    circle_list = []
    circle_one = Circle(10.5)
    print(circle_one)
    #print(circle_one.pi)
    print(circle_one.radius)
    print(circle_one.find_area())
    print(circle_one.x)
    print(circle_one.y)
    circle_blue = Circle(5.3,5,7,"blue") # positional arguments
    print(circle_blue.color)
    print(circle_blue.area)
    circle_red = Circle(x=34,y=56,color="red") # keyword arguments
    print(circle_red.radius)
    print(circle_red.area)
    print(circle_one)
    print(circle_blue)
    print("inside main" + str(dir()))
    #print(z)
    circle_list.append(circle_one)
    circle_list.append(circle_blue)
    circle_list.append(circle_red)
    for i in range(10):
        circle_list.append(Circle(randint(1,10),randint(1,100)))
    for i in range(len(circle_list)):
        print(circle_list[i])
main()
print("outside main" + str(dir()))
z = 10



#print(dir())

#def__init__(self,
#"self" refers to the object itself

#The 2 underscores (__) in a function name make this known as a magic name
