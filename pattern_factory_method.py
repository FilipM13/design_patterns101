"""
Factory method. Specific Creator classes inherit from general Creator classes to maintain it's logic but return different type of object.
In this case common logic for different Creator classes is .speak() and .grow_fur().
Every class can add it's own logic and returns different type of object.
Returned objects must inherit from same base class (here: Dog, Cat, Worm and Hyena inherit from Animal class).
"""
from abc import ABC, abstractmethod

class Animal(ABC):
  """
  General animal class.
  """

  count = 0
  @abstractmethod
  def __init__(self, weight, hunger, mood):
    Animal.count += 1
    self.weight = weight
    self.hunger = hunger
    self.mood = mood

  def speak(self):
    print('>general animal sound<')

  def feed(self, *args):
    if self.hunger == 0:
      print('I\'m not hungry.')
    else:
      self.hunger -= 1
      if self.hunger < 0:
        self.hunger = 0
      print('Nice food.')

  def grow_fur(self):
    print(self.__class__.__name__, 'has fur now.')
    self.weight += 0.5

  def __repr__(self):
    answer = list()
    answer.append(self.__class__.__name__)
    for i in self.__dict__.keys():
      answer.append(f'{i}: {self.__dict__[i]}')
    return '\n'.join(answer)

class Dog(Animal):
  """
  Class for creating dogs. Inherits from Animal class.
  """

  count = 0

  def __init__(self, breed, likes_cats, weight, hunger, mood):
    super().__init__(weight, hunger, mood)
    self.breed = breed
    self.likes_cats = likes_cats
    self.can_bite = bool()
    Dog.count += 1

  def speak(self):
    print('WOOF')

  def grow_teeth(self):
    print('Dog can bite now.')
    self.can_bite = True
  
class Cat(Animal):
  """
  Class for creating cats. Inherits from Animal class.
  """

  count = 0

  def __init__(self, breed, likes_dogs, weight, hunger, mood):
    super().__init__(weight, hunger, mood)
    self.breed = breed
    self.likes_dogs = likes_dogs
    self.can_scratch = bool()
    Cat.count += 1

  def speak(self):
    print('MEOW')

  def feed(self):
    super().feed()
    print('*barf*')
    print('Give me more food.')

  def grow_claw(self):
    print('Cat can scratch now.')
    self.can_scratch = True

class Worm(Animal):

  count = 0

  def __init__(self, food, weight, hunger, mood):
    super().__init__(weight, hunger, mood)
    self.food = food
    Worm.count += 1

  def feed(self, food):
    if food == self.food:
      super().feed()
    
  def speak(self):
    print('I\'m not much of a talker.')

  def grow_fur(self):
    super().grow_fur()
    print('I am worm, I don\'t want fur.')
    self.weight -= 0.5
    self.weight = round(self.weight, 2)

class Hyena(Animal):

  count = 0

  def __init__(self, weight, hunger, mood):
    super().__init__(weight, hunger, mood)
    self.can_hunt = bool()
    Hyena.count += 1

  def speak(self):
    print('XDXDXDXDXD')

  def learn_hunting(self):
    print('Hyena can hunt now.')
    self.can_hunt = True


class Creator(ABC):
  """
  General creator class.
  """
  @classmethod
  @abstractmethod
  def create(cls, rv):
    rv.grow_fur()
    rv.speak()
    pass

class DogCreator(Creator):
  """
  Dog creator class.
  """

  @classmethod
  def create(cls):
    rv = Dog('labrador', likes_cats=True, weight=25, hunger=8, mood=0.9)
    print('Dog created.')
    rv.grow_teeth()
    rv.feed()
    super().create(rv)
    return rv

class CatCreator(Creator):
  """
  Cat creator class.
  """

  @classmethod
  def create(cls):
    rv = Cat('persian', likes_dogs=False, weight=5, hunger=5, mood=0.5)
    print('Cat created.')
    rv.grow_claw()
    rv.feed()
    super().create(rv)
    return rv

class WormCreator(Creator):
  """
  Cat creator class.
  """

  @classmethod
  def create(cls):
    rv = Worm('leaves', weight=0.1, hunger=5, mood=0.5)
    print('Worm created.')
    rv.feed('leaves')
    super().create(rv)
    return rv

class HyenaCreator(Creator):
  """
  Hyena creator class.
  """

  @classmethod
  def create(cls):
    rv = Hyena(weight=35, hunger=7, mood=0.4)
    print('Hyena created.')
    rv.feed()
    rv.learn_hunting()
    super().create(rv)
    return rv

'''#uncomment for demonstration
doge = DogCreator.create()
print()
cate = CatCreator.create()
print()
joe = WormCreator.create()
print()
bob = HyenaCreator.create()

print(bob)
'''
