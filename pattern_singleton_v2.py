'''
Singleton. This pattern allows global access to one instance.
This version of Singleton prevents creating more than 1 instance of a class.
here: 
    Database - Singleton
    users - ways to access Database
'''

class Database():
  instance = None

  def __new__(cls):
    if not isinstance(cls.instance, Database): 
      rv = super().__new__(cls)
      cls.instance = rv
      return rv
    else: 
      return cls.instance

  @classmethod
  def get_instance(cls):
    if isinstance(cls.instance, Database):
      return cls.instance
    else:
      cls.instance = Database()
      return cls.instance

  def add_atr(self, atr_name, atr_value):
    self.__setattr__(atr_name, atr_value)

'''#uncomment for demonstration

x = Database()
y = Database()

print(x)  #this
print(y)  #and this
          #are the same object

user_first = Database.get_instance() #gets x 
user_first.add_atr('name', 'what')  #adds atribute 'name' to x
print(user_first.name)
print(user_first)

user_second = Database.get_instance()
print(user_second)
print(user_second.name)
print(user_first)
print(user_first.name)
print(x.name)
'''