'''
Visitor. Separates behavior from object itself.
here:
  Box, 
  Sphere - objects with similarities (shape)
  VolumeVisitor,
  AreaVisitor - visitors that perform action on objects
'''
from abc import ABC, abstractmethod
from math import pi

class GeneralObject(ABC):

  @abstractmethod
  def __init__(self, *shape):
    pass

class Box(GeneralObject):

  def __init__(self, x, y, z):
    self.shape = (x, y, z)

class Sphere(GeneralObject):

  def __init__(self, radius):
    self.radius = radius


class GeneralVisitor(ABC):

  @abstractmethod
  def __init__(self):
    pass

class VolumeVisitor(GeneralVisitor):

  def __init__(self):
    super().__init__()

  def calculate_volume_box(self, box_object: Box):
    rv = box_object.shape[0] * box_object.shape[1] * box_object.shape[2]
    return rv

  def calculate_volume_sphere(self, sphere_object: Sphere):
    rv = 4/3 * pi * sphere_object.radius**3
    return round(rv, 2)

class AreaVisitor(GeneralVisitor):

  def __init__(self):
    super().__init__()

  def calculate_area_box(self, box_object: Box):
    rv = 2 * ( box_object.shape[0] * box_object.shape[1] + box_object.shape[1] * box_object.shape[2] + box_object.shape[0] * box_object.shape[2] )
    return rv
  
  def calculate_area_sphere(self, sphere_object: Sphere):
    rv = 4 * pi * sphere_object.radius ** 2
    return round(rv, 2)


'''#uncomment for demonstration

b = Box(5, 1, 2)
s = Sphere(10)

vv = VolumeVisitor()
av = AreaVisitor()

print(av.calculate_area_box(b))
print(vv.calculate_volume_box(b))

print(av.calculate_area_sphere(s))
print(vv.calculate_volume_sphere(s))
'''