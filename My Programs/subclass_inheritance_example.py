#subclass_inheritance_example.py

from math import pi

class Shape(): # superclass
    def __init__(self,dim):
        self.dim = dim
    def __str__(self):
        return "Shape object with dim = " + str(self.dim)

class Square(shape): # Square is a subclass of Shape
    def __init__(self,dim):
        Shape.__init__(self,dim)
        self.area = self.findArea()
    def findArea(self):
        self.area = self.dim ** 2
        return self.area
    def __str__(self):
        return "Square object area = " + str(self.findArea()) + \
               " has dim = " + str(self.dim)

class Rectangle(Shape): # Rectangle is a subclass of Shape
    def __init__(self,width,height):
        Shape.__init__(self,width)
        self.height = height
        self.area = self.findArea()
    def findArea(self):
        self.area = self.dim * self.height
        return self.area
    def __str__(self):
        return "Rectangle object area = " + str(self.findArea()) + \
               " has dim = " + str(self.dim) + " has height " + str(self.height)

class Circle(Shape): # Circle is a subclass of Shape
    def __init__(self,dim):
        Shape.__init__(self,dim)
        self.area = self.findArea()
    def findArea(self):
        self.area = pi * self.dim ** 2
        return self.area
    def __str__(self):
        return "Circle object area = " + str(self.findArea()) + \
               " has dim = " + str(self.dim)

class Sphere(Shape): # Sphere is a subclass of Shape
    def __init__(self,dim):
        Shape.__init__(self,dim)
        self.area = self.findArea()
        self.volume = self.findVolume()
    def findArea(self): # surface area
        self.area = 4 * pi * self.dim ** 2
        return self.area
    def findVolume(self):
        self.volume = 4/3 * pi * self.dim ** 2
    def __str__(self):
        return "Sphere object area = " + str(self.findArea()) + \
               " has dim = " + str(self.dim)

def main():
    shape_list = []
    shape_list.append(Square(10))
    shape_list.append(Rectangle(15,20))
    shape_list.append(Circle(5))
    shape_list.append(Sphere(10))

    for i in range(len(shape_list)):
        print(shape_list[i])
        print("area is " + str(shape_list[i].findArea()))
        print("dim is " + str(shape_list[i].dim))
        if ininstance(shape_list[i],Sphere):
            print("volume is " + str(shape_list[i].findVOlume()))

main()
