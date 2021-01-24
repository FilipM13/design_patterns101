'''
Bridge. Structure simplifying code by deviding one object type into 2 hierarchies.
It helps solving cartesian product problem.
Example:
  In this case if I want to create one class for every combination of plane and ownership i'd need 16 classes (4 planes x 4 ownerships)
  Thanks to  bridge pattern I only have 8 classes. It works even better if there where more types of planes and ownerships.
here:
  Main hierachy is Plane (with subclasses), it uses Ownership hierarchy to expand it's possibilities.

PS. I don't care that you can't have private bomber.
'''
from abc import ABC, abstractmethod, abstractclassmethod


class Ownership(ABC):

  def __init__(self, owner_name):
    self.owner_name = owner_name

  def get_owner_name(self):
    return self.owner_name

class Civil(Ownership):

  def __init__(self, owner_name):
    super().__init__(owner_name)
    self.velocity_multiplier = 3

class Private(Ownership):

  def __init__(self, owner_name):
    super().__init__(owner_name)
    self.velocity_multiplier = 7

class Military(Ownership):

  def __init__(self, owner_name):
    super().__init__(owner_name)
    self.velocity_multiplier = 10

class PublicTransport(Ownership):

  def __init__(self, owner_name):
    super().__init__(owner_name)
    self.velocity_multiplier = 5


class Plane(ABC):

  def __init__(self, ownership: Ownership):
    self.ownership = ownership

  def fly(self):
    print(f'WHOOOOOOOSH! with the speed of {self.ownership.velocity_multiplier * self.max_velocity} distance units / time unit.')

  def get_owner_name(self):
    return self.ownership.get_owner_name()

class Jet(Plane):

  def __init__(self, ownership: Ownership):
    super().__init__(ownership)
    self.max_velocity = 100

class Airbus(Plane):

  def __init__(self, ownership: Ownership):
    super().__init__(ownership)
    self.max_velocity = 50

class Bomber(Plane):

  def __init__(self, ownership: Ownership):
    super().__init__(ownership)
    self.max_velocity = 70

class Glider(Plane):

  def __init__(self, ownership: Ownership):
    super().__init__(ownership)
    self.max_velocity = 30


'''#uncomment for demonstration

civil_bomber = Bomber(Civil('Retired bomber pilot.'))
civil_bomber.fly()
print(civil_bomber.get_owner_name())

private_jet = Jet(Private('Ash Holle Rich'))
private_jet.fly()
print(private_jet.get_owner_name())

'''