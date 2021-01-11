class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height

  def get(self):
    return self.radius 

  def set(self,radius):
    self.radius = radius
    
  def base_area(self):
    import math
    return (self.radius**2)*math.pi

  def surface_area(self):
    import math
    return 2*math.pi*self.radius*self.height
  def area(self):
    return 2*self.base_area()+self.surface_area()

  def volume(self):
    return self.base_area()*self.height

cylinder1 = Cylinder(radius=3,height=5)
print(cylinder1.area())
print(cylinder1.volume())