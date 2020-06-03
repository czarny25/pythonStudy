'''
Created on 1 Jun 2020

@author: czarn
'''

''' docstrings example '''


def myDocstring(a):
    "this is one hell of a docstring"
    return a

# this is how to use docstring 
help(myDocstring)

''' this method - __doc__  stores metadata string '''
print(myDocstring.__doc__) 


''' Annotation methods '''

def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
    return a * b
print(my_func("2", 3))

help(my_func)

''' this method - __annotations__  stores metadata string '''
print(my_func.__annotations__)






























