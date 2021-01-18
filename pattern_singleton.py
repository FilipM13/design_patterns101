'''
Singleton. This pattern allows global access to one instance.
here: 
    Database - Singleton
    users - ways to access Database
'''
class Database():
  instance = None

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

user_first = Database.get_instance()
user_first.add_atr('name', 'what')
print(user_first.name)
print(user_first)

user_second = Database.get_instance()
print(user_second)
print(user_second.name)
print(user_first)
print(user_first.name)
'''