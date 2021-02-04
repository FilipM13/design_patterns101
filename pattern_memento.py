'''
Memento. Pattern that allows saving state of object. Later this state can be recovered.
here:
  document - object that can be midified
  memento - class of states
'''

class Memento():

  def __init__(self, doc):
    self.text = doc.text
    self.font = doc.font
    self.size = doc.size

  def recover(self):
    return self.__dict__

class Document():

  def __init__(self, text, font, size):
    self.text = text
    self.font = font
    self.size = size

  def save_state(self):
    return Memento(self)

  def recover_last_state(self, state):
    self.__dict__ = state.recover()

  def __repr__(self):
    txt = []
    for k, v in self.__dict__.items():
      txt.append(f'{k}: {v}')
    return '\n'.join(txt)


'''#uncomment for demonstration

goodbook = Document('This is pretty good book.', 'Times', 250)
print(goodbook, '\n')
copy1 = goodbook.save_state()

goodbook.size = 300
goodbook.text += ' A change that seems ok.'
copy2 = goodbook.save_state()

goodbook.font = 'Sans Terrible'
goodbook.text += ' Now it seems more terrible.'
copy3 = goodbook.save_state()

goodbook.text = 'After changes it\'s terrible book'
goodbook.font = 'Comic'
print(goodbook, '\n')

goodbook.recover_last_state(copy1)
print(goodbook, '\n')

goodbook.recover_last_state(copy2)
print(goodbook, '\n')

goodbook.recover_last_state(copy3)
print(goodbook, '\n')

goodbook.recover_last_state(copy1)
print(goodbook, '\n')
'''