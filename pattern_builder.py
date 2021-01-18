'''
Builders and Director. For creating many differat versions of the same object we ecstract their atributes from base class.
We create Builder classes that sets different values to these atributes.
To automate creating object where different Builders are required we create Director class 
where each method uses different Builders and returns complete object.
here:
object - Car
builders - Builder, SportBuilder, TerrainBuilder, SuvBuilder
director - Director:
    - builds sport suv - combines SportBuilder and SuvBuilder
    - builds semi offroad - combines TerrainBuilder, SuvBuilder, Builder
'''

class Car():

  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    answer = []
    answer.append(self.__class__.__name__)
    for i in self.__dict__.keys():
      answer.append(f'{i}: {self.__dict__[i]}')
    return '\n'.join(answer)

class Builder():

  @classmethod
  def set_wheels(cls, obj: Car):
    obj.wheels = 'street'

  @classmethod
  def set_suspension(cls, obj: Car):
    obj.suspension = 'street'

  @classmethod
  def set_horse_power(cls, obj: Car):
    obj.horse_power = 150

  @classmethod
  def set_engine_cc(cls, obj: Car):
    obj.engine = 1200

class SportBuilder(Builder):

  @classmethod
  def set_wheels(cls, obj: Car):
    obj.wheels = 'slick'

  @classmethod
  def set_suspension(cls, obj: Car):
    obj.suspension = 'hard'

  @classmethod
  def set_horse_power(cls, obj: Car):
    obj.horse_power = 350

  @classmethod
  def set_engine_cc(cls, obj: Car):
    obj.engine = 2000

class TerrainBuilder(Builder):

  @classmethod
  def set_wheels(cls, obj: Car):
    obj.wheels = 'offroad'

  @classmethod
  def set_suspension(cls, obj: Car):
    obj.suspension = 'terrain'

  @classmethod
  def set_horse_power(cls, obj: Car):
    obj.horse_power = 350

  @classmethod
  def set_engine_cc(cls, obj: Car):
    obj.engine = 3000

class SuvBuilder(Builder):

  @classmethod
  def set_wheels(cls, obj: Car):
    obj.wheels = 'street'

  @classmethod
  def set_suspension(cls, obj: Car):
    obj.suspension = 'street'

  @classmethod
  def set_horse_power(cls, obj: Car):
    obj.horse_power = 200

  @classmethod
  def set_engine_cc(cls, obj: Car):
    obj.engine = 1800

'''#uncomment for demonstration

regular = Car(name='regular car')
Builder.set_wheels(regular)
Builder.set_suspension(regular)
Builder.set_horse_power(regular)
Builder.set_engine_cc(regular)
print(regular)

sport = Car(name='speed')
SportBuilder.set_suspension(sport)
SportBuilder.set_wheels(sport)
SportBuilder.set_horse_power(sport)
SportBuilder.set_engine_cc(sport)
print(sport)

buggy = Car(name='beach buggy')
TerrainBuilder.set_wheels(buggy)
TerrainBuilder.set_suspension(buggy)
TerrainBuilder.set_horse_power(buggy)
TerrainBuilder.set_engine_cc(buggy)
print(buggy)

big_boy = Car(name='important bussinessman')
SuvBuilder.set_suspension(big_boy)
SuvBuilder.set_wheels(big_boy)
SuvBuilder.set_horse_power(big_boy)
SuvBuilder.set_engine_cc(big_boy)
print(big_boy)
'''

class Director():

  @classmethod
  def make_sport_suv(cls, name):
    rv = Car(name=name)
    SportBuilder.set_engine_cc(rv)
    SportBuilder.set_horse_power(rv)
    SuvBuilder.set_suspension(rv)
    SuvBuilder.set_wheels(rv)
    return rv

  @classmethod
  def make_semi_offroad(cls, name):
    rv = Car(name=name)
    TerrainBuilder.set_engine_cc(rv)
    SuvBuilder.set_horse_power(rv)
    Builder.set_suspension(rv)
    Builder.set_wheels(rv)
    return rv

'''#uncomment for demonstration

sport_suv = Director.make_sport_suv('fast important bussinessman')
print(sport_suv)

city_jeep = Director.make_semi_offroad('suburb citizen')
print(city_jeep)
'''
