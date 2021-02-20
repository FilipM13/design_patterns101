"""
State. Pattern that allows changing behaviour of object by defining it's states.
here:
  Document - object with 3 possible states (creation, verification and published)
"""

class Document:

  def __init__(self):
    self._text = None
    self._state = 'creation'

  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, new: str):
    if self._state == 'creation':
      self._text = new
    else:
      print('You can\'t change text now.')
      self._text = self._text

  @property
  def state(self):
    return self._state
  @state.setter
  def state(self, new):
    if new not in ['creation', 'verification', 'published']:
      print('Incorrect new state.')
    elif self._state == 'published' and new == 'verification':
      print('Can\'t change state to verification')
    else:
      print(f'State changed from {self._state} to {new}.')
      self._state = new

  def next_state(self):
    if self.state == 'creation':
      print('Document passed for verification.')
      self.state = 'verification'
    elif self.state == 'verification':
      print('Document published.')
      self.state = 'published'
    elif self.state == 'published':
      print('Document in final state.')

  def published_to_creation(self):
    print('Document can be modified now.')
    self.state = 'creation'

  def new_text(self, text):
    self.text = text

'''# uncomment for demonstration
doc1 = Document()
doc1.new_text('Ayy gfo blblblblbl')
print(doc1.text)
doc1.next_state()
doc1.new_text('glglglglglglglglgl')
doc1.next_state()
doc1.next_state()
doc1.next_state()
doc1.published_to_creation()
doc1.new_text('It\' wednesday my dudes... AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.')
doc1.state = 'publishe'
doc1.state = 'published'
'''