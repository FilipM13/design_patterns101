"""
Simple factory. Creator class returns different type of object depending on input.
Using creator simplifies using of Animal subclasses. User doesn't know how 'animal' is created.
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

  def feed(self):
    if self.hunger == 0:
      print('I\'m not hungry.')
    else:
      self.hunger -= 1
      if self.hunger < 0:
        self.hunger = 0
      print('Nice food.')

  def grow_furr(self):
    self.weight += 0.5

  def __repr__(self):
    answer = []
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
    Dog.count += 1

  def speak(self):
    print('WOOF')
  
class Cat(Animal):
  """
  Class for creating cats. Inherits from Animal class.
  """

  count = 0

  def __init__(self, breed, likes_dogs, weight, hunger, mood):
    super().__init__(weight, hunger, mood)
    self.breed = breed
    self.likes_dogs = likes_dogs
    Cat.count += 1

  def speak(self):
    print('MEOW')

  def feed(self):
    super().feed()
    print('*barf*')
    print('Give me more food.')

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

  def grow_furr(self):
    super().grow_furr()
    print('I am worm, I dont want furr.')
    self.weight -= 0.5
    self.weight = round(self.weight, 2)

class Hyena(Animal):

  count = 0

  def __init__(self, weight, hunger, mood):
    super().__init__(weight, hunger, mood)
    Hyena.count += 1

  def speak(self):
    print('XDXDXDXDXD')

class AnimalCreator:
  """
  Simple factory for creating Animals.
  """

  @classmethod
  def create_animal(cls, a_type):
    
    if a_type == 'dog':
      rv = Dog(breed='retriever', likes_cats=False, weight=25, hunger=8, mood=0.9)
    elif a_type == 'cat':
      rv = Cat('persian', likes_dogs=False, weight=3, hunger=5, mood=0.5)
    elif a_type == 'worm':
      rv = Worm(food='leafs', weight=0.1, hunger=5, mood=5)
    elif a_type == 'hyena':
      rv = Hyena(weight=35, hunger=7, mood=5)
    
    rv.grow_furr()
    rv.speak()
    return rv

'''#uncomment for demonstration

doge = AnimalCreator.create_animal('dog')
catee = AnimalCreator.create_animal('cat')
joe = AnimalCreator.create_animal('worm')
bob = AnimalCreator.create_animal('hyena')

print(bob)

shelter = [AnimalCreator.create_animal('dog') for _ in range(20)]

for dog in shelter: print(dog)
'''