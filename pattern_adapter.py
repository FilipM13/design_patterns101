"""
Adapter or wrapper. Allows 2 objects with different interfaces to interact with each other.
here:
  UsefulBox - client-side available interface
  less_to_ful_adapter - adapter that allows client to perform UsefulBox methods on UselessBox
  UselessBox - client-side unavailable interface
"""

class UsefulBox:

  def __init__(self, color: str, material: str, x: int, y: int, z: int):
    self.color = color
    self.material = material
    self.X = x
    self.Y = y
    self.Z = z

  def get_volume(self):
    return self.X * self.Y * self.Z
    
  def __repr__(self):
    rv = list()
    rv.append(str(self.__class__.__name__))
    for i in self.__dict__.keys():
      rv.append(f'{i} : {self.__dict__[i]}')
    return '\n'.join(rv)

class UselessBox:

  def __init__(self, properties: dict, width: int, height: int, depth: int):
    self.properties = properties
    self.width = width
    self.height = height
    self.depth =depth

  def gimme_volume(self):
    return self.width * self.height * self.depth

  def __repr__(self):
    rv = list()
    rv.append(str(self.__class__.__name__))
    for i in self.__dict__.keys():
      rv.append(f'{i} : {self.__dict__[i]}')
    return '\n'.join(rv)

class LessToFulAdapter:

  def __init__(self, useless_box):
    self.instance = useless_box

  def get_volume(self):
    return self.instance.gimme_volume()

  def __repr__(self):
    return str(self.instance)

'''#uncomment for demonstration

print('\nregular useful object:\n')
usf = UsefulBox('red', 'metal', 10, 5, 6) #useful object and it's representation
print(usf)
print(usf.get_volume())

print('\nregular useless object:\n')
usl = UselessBox({'color': 'white', 'material': 'metal'}, 3, 4, 5) #useless object and it's representation
print(usl)
print(usl.gimme_volume())

print('\nadapted useless object:\n')
x = LessToFulAdapter(usl)
print(x)
print(x.get_volume())
'''