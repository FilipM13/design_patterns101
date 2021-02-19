"""
Iterator. Allows iterating in specific way through custom structure.
here:
  Tree (and subclasses) - structure (based on composite pattern)
  TreeIterator - class allowing to iterate through Tree structure
"""
from abc import ABC, abstractmethod

class Tree(ABC):
  pass

class Branch(Tree):

  def __init__(self):
    self.elements = list()

  def add_element(self, element):
    self.elements.append(element)

  def __repr__(self):
    return str(self.elements)

class Leaf(Tree):

  def __init__(self, value):
    self.value = value

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

  def __repr__(self):
    return str(self.value)

class TreeIterator(ABC):

  def __init__(self, tree: Tree):
    self.tree = tree
    pass

  def show(self):
    rv = '['
    for i, t in enumerate(self.tree.elements):
      rv += f'\nBranch {i}: ' + str(t)
    return rv+'\n]'


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

iterator = TreeIterator(b3)
print(iterator.show())

b3.add_element(l1)
print(iterator.show())
'''