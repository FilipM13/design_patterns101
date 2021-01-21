'''
Proxy. Structure that hides actions from client. Proxy and original object share the same interface.
Proxy allows performing actions on original object when it's unavailable.
here:
  Service - common interface
  BankAccount - service target object
  Card - proxy for BankAccount providing extra feature of access check
'''
from abc import ABC, abstractmethod, abstractclassmethod

class Service(ABC):
  '''
  Interface.
  '''
  def __init__(self):
    pass

  def take(self):
    pass

  def add(self):
    pass


class BankAccount(Service):
  '''
  Accual service object.
  '''
  def __init__(self, account_number, money, dept, pin, available):
    self.pin = pin
    self.account_number = account_number
    self.money = money
    self.dept = dept
    self.available =available
  
  def take(self, amout):
    self.money -= amout
    if self.money < 0:
      self.dept -= self.money
      self.money = 0

  def add(self, amout):
    self.dept -= amout
    if self.dept < 0:
      self.money += self.dept
      self.dept = 0


class Card(Service):
  '''
  BankAccount proxy.
  '''
  def __init__(self, account):
    self.account = account

  def take(self, amount, pin):
    if self.account.pin == pin and self.account.available:
      self.account.take(amount)
      print('Action successful.')
    elif self.account.pin != pin:
      print('Wrong pin code.')
    else:
      print('Action unavailable.')

  def add(self, amount, pin):
    if self.account.pin == pin and self.account.available:
      self.account.add(amount)
      print('Action successful.')
    elif self.account.pin != pin:
      print('Wrong pin code.')
    else:
      print('Action unavailable.')


'''#uncomment for demonstration

Janusz_Tracz = BankAccount(123456789, 10000, 0, '0997', True)
karta_Janusza_Tracza = Card(Janusz_Tracz)

karta_Janusza_Tracza.add(100, '0997')
karta_Janusza_Tracza.add(50, '0994')

karta_Janusza_Tracza.take(6500, '0997')
karta_Janusza_Tracza.take(500, '0979')

#bank manager notices there is something wrong with the account and blocks it:
Janusz_Tracz.available = False

#client tries to make some actions
karta_Janusza_Tracza.add(100, '0997')
karta_Janusza_Tracza.add(50, '0994')

karta_Janusza_Tracza.take(6500, '0997')
karta_Janusza_Tracza.take(500, '0979')
#Janusz Tracz is mad
'''