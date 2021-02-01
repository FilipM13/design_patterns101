'''
Template. Allows defining main logic in superclass and override it in subclasses that share common parts.
here:
  Animal - main class for basic logic
  Dog, Cat, worm, Hyena - subclasses that inherit main logic from Animal class for further use or modification
'''
from abc import ABC, abstractclassmethod, abstractmethod

class Animal(ABC):
  '''
  General animal class.
  '''

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
  '''
  Class for creating dogs. Inherits from Animal class.
  '''

  count = 0

  def __init__(self, breed, likes_cats, weight, hunger, mood):
    super().__init__(weight, hunger, mood)
    self.breed = breed
    self.likes_cats = likes_cats
    Dog.count += 1

  def speak(self):
    print('WOOF')
  
class Cat(Animal):
  '''
  Class for creating cats. Inherits from Animal class.
  '''

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


'''#uncomment for demonstration

Baster = Dog('rotweiler', False, 30, 0.5, 0.5)
Baster.grow_furr()
Baster.speak()
print(Baster, '\n')

Luna = Cat('Persian', False, 5, 0.6, 0.3)
Luna.grow_furr()
Luna.speak()
print(Luna)
'''