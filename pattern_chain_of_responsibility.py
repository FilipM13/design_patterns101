'''
Chain of responsibility. Pattern that allows passing one request along many linked objects (handlers). 
Each handler decides if it should pass it to the next handler or do something else.
here:
  BaseHandler - abstract class for every chain link, with implementation for initialization and operations
  AuthorizHandler,
  ConfirmeHandler,
  VerifyHandler,
  BossHandler,
  ReturnHandler - chain links inheriting from BaseHandler
'''
from abc import ABC, abstractmethod

class BaseHandler(ABC):

  @abstractmethod
  def __init__(self, next_handler=None):
    self.next_handler = next_handler

  @abstractmethod
  def task(self, *args, **kwargs):
    pass

  def set_handler(self, next_handler):
    self.next_handler = next_handler

class AuthorizeHandler(BaseHandler):

  def __init__(self, next_handler=None):
    super().__init__(next_handler)

  def task(self, *args, **kwargs):
    if kwargs['authorized'] == True and self.next_handler != None:
      print('Authorized.')
      self.next_handler.task(*args, **kwargs)
    else:
      print('END')

class VerifyHandler(BaseHandler):

  def __init__(self, next_handler=None):
    super().__init__(next_handler)

  def task(self, *args, **kwargs):
    if kwargs['verified'] == True and self.next_handler != None:
      print('Verified.')
      self.next_handler.task(*args, **kwargs)
    else:
      print('END')

class ConfirmHandler(BaseHandler):

  def __init__(self, next_handler=None):
    super().__init__(next_handler)

  def task(self, *args, **kwargs):
    if kwargs['confirmed'] == True and self.next_handler != None:
      print('Confirmed.')
      self.next_handler.task(*args, **kwargs)
    else:
      print('END')

class BossHandler(BaseHandler):

  def __init__(self, next_handler=None):
    super().__init__(next_handler)

  def task(self, *args, **kwargs):
    if kwargs['boss'] == True:
      print('You da boss.')
      self.next_handler.task(*args, **kwargs)
    else:
      print('END')

class ReturnHandler(BaseHandler):

  def __init__(self, next_handler=None):
    super().__init__(next_handler)

  def task(self, *args, **kwargs):
    print('You got to the end with full access.')


'''#uncomment for demonstration

a = AuthorizeHandler()
v = VerifyHandler()
c = ConfirmHandler()
b = BossHandler()
r = ReturnHandler()

a.set_handler(v)
v.set_handler(c)
c.set_handler(r)
b.set_handler(r)

a.task(verified=True, authorized=True, confirmed=True)
b.task(boss=True)

'''