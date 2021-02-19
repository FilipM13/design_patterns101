"""
Mediator. Pattern that allows reducing chaos by organizing interactions between objects.
here:
  Component, ConcreteComponent1, ConcreteComponent2 - objects that interact with each other
  Mediator, SingleMediator, DoubleMediator - mediators
"""
from abc import ABC, abstractmethod
import random

class Component(ABC):

  def __init__(self, name: str, mediator = None):
    self._name = name
    self._mediator = mediator

  @property
  def mediator(self):
    return self._mediator
  @mediator.setter
  def mediator(self, mediator):
    self._mediator = mediator

  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, name):
    self._name = name

  @abstractmethod
  def func(self, *args):
    pass

class ConcreteComponent1(Component):

  def func(self, n):
    self._mediator.notify(self.name)
    return ['x' for _ in range(n)]

class ConcreteComponent2(Component):

  def func(self):
    return random.randint(1,11)

class Mediator(ABC):

  @abstractmethod
  def action(self, request: str):
    pass

  def notify(self, name):
    print(f'I got notified by {name}.')

class SingleMediator(Mediator):

  def __init__(self, component):
    self.component = component
    self.component.mediator = self

  def action(self, request: str):
    if request == 'a':
      print('Starting generating:')
      rv = self.component.func(5)
      print('Generating finished.')
      return rv
    elif request == 'b':
      print('Starting generating:')
      rv = self.component.func(7)
      print('Generating finished.')
      return rv
    elif request == 'c':
      print('Starting generating:')
      rv = self.component.func(10)
      print('Generating finished.')
      return rv

class DoubleMediator(Mediator):

  def __init__(self, component1: ConcreteComponent1, component2: ConcreteComponent2):
    self.component1 = component1
    self.component1.mediator = self
    self.component2 = component2
    self.component2.mediator = self

  def action(self, request: str):
    if request == 'a':
      print('Starting generating:')
      rv = self.component1.func(5)
      print('Genereting finished.')
      return rv
    elif request == 'xy':
      print('Starting generating:')
      n = self.component2.func()
      rv = self.component1.func(n)
      print('Genereting finished.')
      return rv


'''# uncomment for demonstration
c1 = ConcreteComponent1('Adam')
c2 = ConcreteComponent2('Eve')
m1 = SingleMediator(c1)
m2 = DoubleMediator(c1, c2)
print(m1.action('a'))
print(m2.action('xy'))
'''