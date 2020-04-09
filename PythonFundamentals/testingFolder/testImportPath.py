'''
Created on 9 Apr 2020

@author: Marty
'''

print("Foo")

from importFundamentals import importPath

p1 = importPath.pinSysDirect12()
p2 = importPath.pinSysDirect22()

def comparePath():
    if p1 == p2:
        print("True")