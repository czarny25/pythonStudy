'''
Created on 14 Apr 2020

@author: czarn
'''


import numpy as np # numpy is external library and need to be imported


# simple list 
list = [1,2,3]

# variable of numpy array type take list as argument
x = np.array(list)

print(type(x))
print(x)

# this is how numpy array turn multidementional array into matrix
myMatrix = [[1,2,3],[3,4,6],[3,6,9]]
print(np.array(myMatrix))
