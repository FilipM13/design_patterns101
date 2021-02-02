'''
Observer. Pattern that allows notifying other objects about taken action.
here:
  Subscriber - class which instances are to be notified
  Channel - class which instances are to notify Subscribers
'''
from abc import ABC, abstractmethod, abstractclassmethod

class Subscriber():

  def __init__(self, name):
    self.name = name

  def get_notification(self):
    print(f'I, {self.name}, have been notified.')

  def subscribe(self, n):
    print(f'I, {self.name}, subscribed to {n.name}.')
    n.add_subscriber(self)

class Channel():

  def __init__(self, name):
    self.name = name
    self.subscribers = set()

  def add_subscriber(self, subscriber):
    print(f'{self.name} has new subscriber: {subscriber.name}.')
    self.subscribers.add(subscriber)

  def add_subscribers(self, subscribers):
    for subscriber in subscribers:
      print(f'{self.name} has new subscriber: {subscriber.name}.')
    self.subscribers.update(subscribers)

  def notify(self):
    for s in self.subscribers:
      s.get_notification()



'''#uncomment for demonstration

noti1 = Channel('ScieFun')
noti2 = Channel('Top10 Everything')

print()
sub1 = Subscriber('Andrew')
sub1.subscribe(noti1)

print()
sub2 = Subscriber('John')
sub2.subscribe(noti1)

print()
sub3 = Subscriber('Maya')
sub3.subscribe(noti2)

print()
sub4 = Subscriber('Bigchungus420')
sub4.subscribe(noti1)
sub5 = Subscriber('Jesus with a gun')
sub6 = Subscriber('Fenrir')

print()
noti2.add_subscribers([sub4, sub5, sub6])


print('\nnoti1 notifies: ')
noti1.notify()
print('\nnoti2 notifies: ')
noti2.notify()
'''