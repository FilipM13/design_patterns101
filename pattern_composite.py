'''
Composite. Pattern that allows creating tree like structures.
here:
  We can put cars (C) into garage (G) and garage into garage.
  G:
    C
    C
    C
    G:
      C
      C
    G:
      C
      C
      C
      G:
        C
        C
      G:
        C
        C
'''
from abc import ABC, abstractclassmethod, abstractmethod

class Component(ABC):

  @abstractmethod
  def __init__(self, name):
    self.name = name

  def get_name(self):
    return self.name

  def __repr__(self):
    return f'<{self.name}, {type(self).__name__}>'

class Car(Component):

  def __init__(self, name, car_type):
    super().__init__(name)
    self.car_type = car_type
  
  def get_car_type(self):
    return self.car_type

class Garage(Component):

  def __init__(self, name, location):
    super().__init__(name)
    self.location = location
    self.component_list = []

  def add_component(self, component: Component):
    self.component_list.append(component)

  def remove_component(self, component: Component):
    self.component_list.remove(component)
  
  def get_location(self):
    return self.location
  
  def get_component_list(self):
    return self.component_list

'''#uncomment for demonstration

ferrari = Car('Roma', 'sport car')
subaru = Car('Impreza', 'rally')
fiat = Car('fiat500', 'pizza delivery race car')

print(ferrari.get_name())
print(subaru.get_car_type())
print(fiat.get_name(), fiat.get_car_type())

poor_garage = Garage('poor guy\'s garage', 'in some lame place')
poor_garage.add_component(fiat)

print(poor_garage.get_component_list())
print(poor_garage.get_location())
print(poor_garage.get_name())

rich_garage = Garage('rich guy\'s garage', 'next to his house')
rich_garage.add_component(ferrari)
rich_garage.add_component(subaru)
rich_garage.add_component(poor_garage)

print(rich_garage.get_component_list())
print(rich_garage.get_location())
print(rich_garage.get_name())

'''