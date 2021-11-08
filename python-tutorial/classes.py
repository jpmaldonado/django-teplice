import math
class Point:
    def __init__(self, x, y, z=42):
        self.x = x
        self.y = y
        self.z = z
        self.__color = 'red'
    
    def magnitude(self):
        self.magnitude = self.x*self.x+self.y*self.y
        return math.sqrt(self.magnitude)

    def color(self):
        print(self.color)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


p = Point(3,5)
print(p.__color)
print(p.magnitude())
print(p)
