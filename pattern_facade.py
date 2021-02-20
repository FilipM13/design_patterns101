"""
Facade. Structure that uses simple interface to manage complex behavior.
Thanks to facade a client doesn't have to understand complicated logic of a process.
here:
  Product,
  ProductDesign,
  Factory,
  PackingArea - classes interacting with each other and use many methods
  CustomerService - facade class calling all methods to create final result
"""
from copy import copy

class Product:

  def __init__(self, name, price, shape):
    self.name = name
    self.price = price
    self.shape = shape

  def repair(self):
    print(f'{self.name} has been repaired.')
    pass

  def damage(self):
    print(f'{self.name} has been damaged.')
    pass

  def de_other_stuff(self):
    pass

  def increase_price(self, money):
    self.price += money

  def __repr__(self):
    answer = list()
    answer.append(self.__class__.__name__)
    for i in self.__dict__.keys():
      answer.append(f'{i}: {self.__dict__[i]}')
    return '\n'.join(answer)

class ProductDesign:

  @classmethod
  def paint(cls, thing: Product, color, money):
    thing.increase_price(money)
    thing.color = color

  @classmethod
  def style(cls, thing: Product, style, money):
    thing.increase_price(money)
    thing.style = style

class Factory:

  @classmethod
  def craft(cls, original_product: Product, number_of_copies):
    return [copy(original_product) for _ in range(number_of_copies)]

class PackingArea:

  @classmethod
  def pack(cls, list_of_products, money):
    for num, ob in enumerate(list_of_products):
      list_of_products[num].price += money
    return list_of_products

class CustomerService:

  order_count = 0

  def __init__(self):
    self.client_shape = None
    self.client_color = None
    self.client_style = None
    self.client_name = None
    self.client_number = None
    self.order_count = None
    self.original_product = None
    self.products = None

  def take_order(self):
    CustomerService.order_count += 1
    self.client_name = str(CustomerService.order_count) + '# ' + input('What object do you need? ')
    self.client_color = input('What color do you want for object? ')
    self.client_shape = input('What shape do you want for object? ')
    self.client_style = input('What style do you want for object? ')
    self.client_number = int(input('How many object do you want? '))

  def create_order(self, price):
    #create product prototype
    self.original_product = Product(self.client_name, price, self.client_shape)
    #design product
    ProductDesign.paint(self.original_product, self.client_color, self.original_product.price*0.1)
    ProductDesign.style(self.original_product, self.client_style, self.original_product.price*0.1)
    #create copies
    self.products = Factory.craft(self.original_product, self.client_number)
    #pack products
    self.products = PackingArea.pack(self.products, self.original_product.price*0.1)

  def give_order(self):
    print('There\'s your product.')
    return self.products


'''#uncomment for demonstration

cs = CustomerService()
cs.take_order()
cs.create_order(price=30)
objects = cs.give_order()
print(objects[0])
'''