"""
Strategy. Pattern that allows separating action (strategy) from it's user. You can define many strategies that can be used.
here:
  Strategy (and subclasses) - strategies for performing an action
  ActionTaker - user of strategies
"""
from abc import ABC, abstractmethod

class Strategy(ABC):

  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def action(self):
    pass

class Strategy1(Strategy):

  def __init__(self):
    super().__init__()
    pass

  def action(self):
    print('I do some kind of stuff.')
    return 1

class Strategy2(Strategy):

  def __init__(self):
    super().__init__()
    pass

  def action(self):
    print('I do other kind of stuff.')
    return 2

class Strategy3(Strategy):

  def __init__(self):
    super().__init__()
    pass

  def action(self):
    print('I do two kinds of stuff.')
    return [1, 2]

class ActionTaker:

  def __init__(self):
    self._strategy = None

  @property
  def strategy(self):
    return self._strategy
  @strategy.setter
  def strategy(self, strategy: Strategy):
    if isinstance(strategy, Strategy1):
      print(f'Strategy changed from {type(self.strategy)} to {type(strategy)}')
      self._strategy = strategy
    elif isinstance(strategy, Strategy2):
      print(f'Strategy changed from {type(self.strategy)} to {type(strategy)}')
      self._strategy = strategy
    elif isinstance(strategy, Strategy3):
      print(f'Strategy changed from {type(self.strategy)} to {type(strategy)}')
      self._strategy = strategy
    else:
      print('Incorrect strategy.')

  def action(self):
    if self.strategy is not None:
      rv = self.strategy.action()
      return rv


'''# uncomment for demonstration
at = ActionTaker()
s1 = Strategy1()
s2 = Strategy2()
s3 = Strategy3()
at.strategy = s1
print(at.action())
at.strategy = s2
print(at.action())
at.strategy = s3
print(at.action())
'''