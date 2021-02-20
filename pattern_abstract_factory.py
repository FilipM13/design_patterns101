"""
Abstract Factory pattern. Allows creating families of related products that share common interface.
here:
    White Factory can create White Dogs and White Cats, Black Factory can create Black Dogs and Black Cats,
    Cats and Dogs share interface of abstract class Animal
"""
from abc import ABC

class Animal(ABC):

  def __repr__(self):
    answer = list()
    answer.append(self.__class__.__name__)
    for i in self.__dict__.keys():
      answer.append(f'{i}: {self.__dict__[i]}')
    return '\n'.join(answer)

class Cat(Animal):

  def __init__(self, weight=3, hunger=5):
    self.weight = weight
    self.hunger = hunger

  def meow(self):
    print('MEOW')

class WhiteCat(Cat):

  def __init__(self, weight=3, hunger=5):
    super().__init__(weight=weight, hunger=hunger)
    self.colour = 'white'

class BlackCat(Cat):

  def __init__(self, weight=3, hunger=5):
    super().__init__(weight=weight, hunger=hunger)
    self.colour = 'black'

class Dog(Animal):

  def __init__(self, weight=25, hunger=5):
    self.weight = weight
    self.hunger = hunger

  def bark(self):
    print('WOOF')

class WhiteDog(Dog):

  def __init__(self, weight=25, hunger=5):
    super().__init__(weight=weight, hunger=hunger)
    self.colour = 'white'

class BlackDog(Dog):

  def __init__(self, weight=25, hunger=5):
    super().__init__(weight=weight, hunger=hunger)
    self.colour = 'black'


class Factory(ABC):

  @classmethod
  def create(cls):
    pass

class WhiteFactory(Factory):

  @classmethod
  def create_white_dog(cls, weight=3, hunger=5):
    return WhiteDog(weight=weight, hunger=hunger)

  @classmethod
  def create_white_cat(cls, weight=3, hunger=5):
    return WhiteCat(weight=weight, hunger=hunger)

class BlackFactory(Factory):

  @classmethod
  def create_black_cat(cls, weight=3, hunger=5):
    return BlackCat(weight=weight, hunger=hunger)

  @classmethod
  def create_black_dog(cls, weight=3, hunger=5):
    return BlackDog(weight=weight, hunger=hunger)

'''#uncomment for demonstration

whitecat = WhiteFactory.create_white_cat()
blackcat = BlackFactory.create_black_cat()
whitedog = WhiteFactory.create_white_dog()
blackdog = BlackFactory.create_black_dog()

print(whitedog)
'''