'''
Created on 9 Apr 2020

@author: Marty
'''
import sys
import os


def pinSysDirect12():
    # shows where is python installed
    print('\n',sys.prefix)
    

def pinSysDirect22():
    # where are compiled binaries are stored
    print('\n',sys.exec_prefix)    


def showYourCurrentPath():
    # this will show your current path of this file
    print('\n',os.getcwd())


def showAllPath23():
    # this will show all paths available in the system
    for l in sys.path:
        print(l)


# how to add path 
def addPathToLocal():
    pass

# how to delete a path
def removePathLocaly2():
    print("test")


# Install a Package Globally
def removePathLocaly223():
    print("test")


pinSysDirect12()

pinSysDirect22()

showYourCurrentPath()

print(" ") # just break

#showAllPath()