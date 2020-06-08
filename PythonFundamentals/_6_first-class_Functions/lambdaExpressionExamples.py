'''
Created on 6 Jun 2020

@author: czarn

Lambda or annonymus function are simply the other way to create function

'''
from builtins import sorted



lambda s: s[::-1].upper()

def apply_func(x, fn):
    return fn(x)

print(apply_func(5, lambda x: x**2))
print(type(lambda x: x**2))
print((lambda x: x**2))
print(id(apply_func))
f = lambda x, y=34: x**y
print((f(3, 4)))

def apply_func1(fn1, *args):
    return fn1(*args)

print(apply_func1(lambda x, y: x**y, 6, 2))


l = [3,5,2,8,7,1]
print(sorted(l))
print(ord(str(l[0])))






































