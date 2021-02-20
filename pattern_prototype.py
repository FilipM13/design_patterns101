"""
Prototype. Pattern which goal is to copy existing object without knowledge about how it's created.
here:
  clone method - creates copies of self (implementation of prototype pattern)
"""

import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
  @abstractmethod
  def clone(self):
    pass

class CarPrototype(Prototype):

  def clone(self):
    return copy.copy(self)
    
  def __repr__(self):
    answer = list()
    answer.append(self.__class__.__name__)
    for i in self.__dict__.keys():
      answer.append(f'{i}: {self.__dict__[i]}')
    return '\n'.join(answer)


'''#uncomment for demonstration

c = CarPrototype()
c.speed = 100
c.weight = 1200
c.engine = 2000
c.horse_power = 450

d = c.clone()

print(d)
print(c)

'''