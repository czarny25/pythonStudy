'''
Created on 9 Apr 2020

@author: Marty
'''
import sys
import os


def pinSysDirect12():
    # shows where is python installed
    ('\n',sys.prefix)
    

def pinSysDirect22():
    # where are compiled binaries are stored
    ('\n',sys.exec_prefix)
    


def showYourCurrentPath():
    # this will show your current path of this file
    ('\n',os.getcwd())



def showAllPath():
    for l in sys.path:
        print(l)

pinSysDirect12()

pinSysDirect22()

# this is laptop installation pateh C:\Users\czarn\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0

showYourCurrentPath()

print(" ") # just break

showAllPath()


# please install SQLAlchemy for below code by running 'pip install SQLAlchemy' in your terminal
import sqlalchemy
print(sqlalchemy.__version__)



print("Tralala")

print("Tralal  from Github")




