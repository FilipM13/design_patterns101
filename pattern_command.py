"""
Command. Allows passing request as an object to commands.
here:
  Receiver - request object
  Command, Print, Verification - command classes that can execute a method
  Invoker - command caller
"""
from abc import ABC, abstractmethod

class Receiver:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self, x, y, z):
    for j in range(y):
      print('0' * x, *range(1,z))

  def verify(self):
    if self.age >= 18:
      print(f'{self.name} is adult.')
    else:
      print(f'{self.name} is underage.')


class Command(ABC):

  def __init__(self, receiver: Receiver, parameters=None):
    self.receiver = receiver
    self.parameters = parameters
  
  @abstractmethod
  def execute(self):
    pass

class Printer(Command):

  def execute(self):
    self.receiver.show(*self.parameters)

class Verification(Command):

  def execute(self):
    self.receiver.verify()


class Invoker:

  def __init__(self, command: Command):
    self.command = command

  def execute_command(self):
    self.command.execute()


'''#uncomment for demonstration
rec = Receiver('Adam', 21)

cmd1 = Printer(rec, [2,3,9])
cmd2 = Verification(rec)

inv1 = Invoker(cmd1)
inv1.execute_command()

inv2 = Invoker(cmd2)
inv2.execute_command()
'''