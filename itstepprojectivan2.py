import requests
from _ctypes_test import func

help (requests)

class Human:
    pass

def func():
    pass

rq = requests
f1 = func
max = Human

print(requests, __name__)
print(rq, __name__)

print(f1, __name__)
print(func, __name__)

print(Human, __name__)
print(max, __name__)

max2 = Human()
print(type(max2))

print(type(func))

str1 ='python'
print(hasattr(str1, 'reverse'))
print(hasattr(str1, 'index'))

print(callable(f1))
print(callable(max2))

class Driver(Human):
    pass

driver = Driver()

print(isinstance(driver, Driver))
print(isinstance(driver, Human))

import inspect

print(inspect.ismodule(requests))
print(inspect.ismodule(max))
print(inspect.isclass(max))
print(inspect.ismethod(max))

food1 = 'burger'
print(hasattr(food1, 'class')) # False
print(hasattr(food1, 'index')) # True

list1 = [1, 2, 3]
number1 = 15
name = 'Ivan'
print(type(list1))
print(type(number1))
print(type(name))