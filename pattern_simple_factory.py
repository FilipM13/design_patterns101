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

  def feed(self, *args):
    if self.hunger == 0:
      print('I\'m not hungry.')
    else:
      self.hunger -= 1
      if self.hunger < 0:
        self.hunger = 0
      print('Nice food.')

  def grow_fur(self):
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

  def grow_fur(self):
    super().grow_fur()
    print('I am worm, I don\'t want fur.')
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
  def create_dog(cls, breed, likes_cats, weight, hunger, mood):
    """
    Method creating object inheriting from Animal class.
    """
    print(f'Dog has been created and it speaks!')
    rv = Dog(breed, likes_cats, weight, hunger, mood)
    rv.grow_fur()
    rv.speak()
    return rv

  @classmethod
  def create_cat(cls, breed, likes_dogs, weight, hunger, mood):
    """
    Method creating object inheriting from Animal class.
    """
    print(f'Cat has been created and it speaks!')
    rv = Cat(breed, likes_dogs, weight, hunger, mood)
    rv.grow_fur()
    rv.speak()
    return rv

  @classmethod
  def create_hyena(cls, weight, hunger, mood):
    """
    Method creating object inheriting from Animal class.
    """
    print(f'Hyena has been created and it speaks!')
    rv = Hyena(weight, hunger, mood)
    rv.grow_fur()
    rv.speak()
    return rv

  @classmethod
  def create_worm(cls, food, weight, hunger, mood):
    """
    Method creating object inheriting from Animal class.
    """
    print(f'Worm has been created and it speaks!')
    rv = Worm(food, weight, hunger, mood)
    rv.grow_fur()
    rv.speak()
    return rv


'''uncomment for demonstration

doge = AnimalCreator.createDog('retriever', True, 25, 5, 0.9)
cate = AnimalCreator.createCat('persian', False, 4, 1, 0.2)
jelly = AnimalCreator.createWorm('leaves', 0.1, 1, 'None')
bob = AnimalCreator.createHyena(4, 5, 5)

print(bob)

breeds = ['retriever', 'doberman', 'pug']
likes_cats = [True, True, False]
weights = [25, 30, 8]
hungers = [8, 5, 5]
moods = [0.9, 0.5, 0.6]

dogs = list(map(AnimalCreator.createDog, breeds, likes_cats, weights, hungers, moods))

for dog in dogs: print(dog)

'''