import math
class shape:
    def area(self):
      print("Area of shape: ")
 
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius* self.radius

class rectangle(shape):
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    def area(self):
        return self.lenght*self.width

class triangle(shape):
    def __init__(self,base,height):
        self.base = base 
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

c = circle(5)

r = rectangle(10,5) 

t = triangle(7,9)


print("area of circle = ",c.area())
print("area of rectangle = ",r.area())
print("area of triangle = ", t.area())
