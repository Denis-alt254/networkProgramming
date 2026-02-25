import math
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def area(self):
        surface_area = (math.pi*math.pow(self.radius, 2)+ (math.pi* (2*self.radius)* self.height))
        print(f"Surface area = {surface_area:.2f}")
    def volume(self):
        volume = (math.pi*math.pow(self.radius, 2)*self.height)
        print(f"Volume = {volume:.2f}")
        
obj = Cylinder(7, 12)

obj.area()
obj.volume()