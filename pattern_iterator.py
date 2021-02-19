"""
Iterator. Allows iterating in specific way through custom structure.
Here are two implementations of iterator - internal and external. For no reason.
here:
  Tree (and subclasses) - iterable structure (based on composite pattern)
    __next__ method and inheriting from Iterator
  TreeIterator - class allowing to iterate through Tree structure
"""
from abc import ABC
from collections.abc import Iterator

class Tree(ABC):
  pass

class Branch(Tree, Iterator):

  def __init__(self):
    self.elements = list()
    self.position = 0

  def add_element(self, element):
    self.elements.append(element)

  def __repr__(self):
    return str(self.elements)

  def __next__(self):
    try:
      rv = self.elements[self.position]
      self.position += 1
    except IndexError:
      raise StopIteration
    return rv

class Leaf(Tree):

  def __init__(self, value):
    self.value = value

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

  def __repr__(self):
    return str(self.value)

class TreeIterator(Iterator):

  def __init__(self, tree: Branch):
    self.position = 0
    self.tree = tree
    pass

  def show(self):
    rv = '['
    for i, t in enumerate(self.tree.elements):
      rv += f'\nBranch {i}: ' + str(t)
    return rv+'\n]'

  def __next__(self):
    try:
      rv = self.tree.elements[self.position]
      self.position += 1
    except IndexError:
      raise StopIteration
    return rv


'''# uncomment for demonstration
l1 = Leaf(1)
l2 = Leaf('a')
l3 = Leaf([1,2,3])
b1 = Branch()
b2 = Branch()
b3 = Branch()
b4 = Branch()
b5 = Branch()
b6 = Branch()

b1.add_element(l1)
b1.add_element(l2)

b2.add_element(b1)
b2.add_element(l3)

b3.add_element(b2)
b3.add_element(b2)
b3.add_element(l1)

print('\nShowing structure of iterable object:')
iterator = TreeIterator(b3)
print(iterator.show())

print('\nShowing structure of iterable object:')
b3.add_element(l1)
print(iterator.show())

print('\nIterating with internal iterator:')
for i in b3:
  print(i)

print('\nIterating with external iterator:')
for i in iterator:
  print(i)
'''