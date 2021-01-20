'''
Decorator. Structure that allows to expand utility of a function.
In python functions are treated as objects therefore can be passed as arguments/parameters.
Because of that we don't have to create class to add logic to chosen function.
here:
  calculation - function calculating stuff
  printer - decorator that prints arguments, key word arguments and result value of a given function
  useless_adds - decorator that adds useless string to result values of a given function
'''

def printer(f):

  def wrapper(*args, **kwargs):
    #logic that can be added o a function
    rv = f(*args, **kwargs)
    print(f'Entered arguments: {args}')
    print(f'Result value: {rv}')
    return rv

  return wrapper

def useless_adds(f):

  def wrapper(*args, **kwargs):
    #logic that can be added o a function
    rv = f(*args, **kwargs)
    'Did you know that koalas may sleep for 18 to 22 hours?'
    return rv, 'Did you know that koalas may sleep for 18 to 22 hours?'

  return wrapper


'''#uncomment for demonstration
#order in which decorators are applied is important:

#here printer is decorator for useless_adds which is decorator for calculation function
#because of that printer prints arguments of calculation function and result value with added comment
#equivalent to:
#calculation = printer(useless_adds(calculation))

@printer
@useless_adds
def calculation(a,b):
  #basic logic of a function
  return a*b

a = calculation(5,3)


#here useless_adds is decorator for printer which is decorator for calculation function
#because of that printer prints arguments of calculation function and result value without added comment
#equivalent to:
#calculation = useless_adds(printer(calculation))

@useless_adds
@printer
def calculation(a,b):
  #basic logic of a function
  return a*b

a = calculation(5,3)
'''