"""
Flyweight. Helps saving RAM space by deciding object into intrinsic and extrinsic parts. Shared/common parts of many objects are stored as one variable.
example:
we can have many red Ford Mustangs so we store it in variable
anytime someone asks for red Ford Mustang same variable is returned
here:
  Car - class with intrinsic and extrinsic properties
  Flyweights - class managing intrinsic properties
"""

class Car:

  def __init__(self, common_state: str):
    self.common_state = common_state

  def operation(self, owner: str, plates: str):
    print(self.common_state)
    print(f'Owner of this car is {owner}.')
    print(f'Plates of this car are {plates}.')


class Flyweights:

  car_families: dict[str, Car] = {}

  @classmethod
  def create_key(cls, state: dict):
    return '_'.join([str(state[i]) for i in sorted(state)])

  @classmethod
  def add_car_families(cls, states: list):
    for state in states:
      k = Flyweights.create_key(state)
      Flyweights.car_families[k] = Car(k)

  @classmethod
  def list_car_families(cls):
    for k, v in Flyweights.car_families.items():
      print(f'Key: {k}: Value {v}')

  @classmethod
  def get_car_family(cls, state: dict):
    for k in state.keys():
      try:
        k = Flyweights.create_key(state)
        return Flyweights.car_families[k]
      except KeyError:
        Flyweights.add_car_families([state])
        return Flyweights.car_families[k]


'''#uncomment for demonstration
Flyweights.add_car_families([
  {'manufacturer':'Ford', 'model':'Mustang', 'color':'red'},
  {'manufacturer':'Dodge', 'model':'Charger', 'color':'black'},
  {'manufacturer':'Fiat', 'model':500, 'color':'white'}
])

print('\nInitial families:')
Flyweights.list_car_families()

Flyweights.add_car_families([{'manufacturer':'Toyota', 'model':'Supra', 'color':'white'}])

print('\nFamilies after adding Toyota:')
Flyweights.list_car_families()

red_mustang = {'manufacturer':'Ford', 'model':'Mustang', 'color':'red'}

print('\nGetting existing family:')
print(Flyweights.get_car_family(red_mustang))

print('\nCheck existing family:')
print(Flyweights.car_families[Flyweights.create_key(red_mustang)] == Flyweights.get_car_family(red_mustang))

print('\nGetting nonexisting family:')
print(Flyweights.get_car_family({'manufacturer':'Subaru', 'model':'Impreza', 'color':'blue'}))

print('\nFamilies after getting nonexisting family:')
Flyweights.list_car_families()

print('\nGetting car family and performing action on it:')
tuning_car = Flyweights.get_car_family({'manufacturer':'Toyota', 'color':'white', 'model':'Supra'})
tuning_car.operation('Joe Swansonson', 'SPEED1')
'''