'''
Created on 26 Apr 2020

@author: czarn
'''

a = (1,2,3) # one way of createing a tuple


b = 1,2,3

print(type(a))
print(type(b))

'''
above shows that to create tuple you don,t need parentheses but commas 
'''

c = 1, # this is tuple as well

print(type(c))

# empty tuple
e = ()
print(type(e))

''' unpacking is also called parallel  assignment'''

a,b,c = [1,2,3]

print(a)
print(b)
print(c)


a,b,c = 34, 45.78, "toup toup"

print(a)
print(b)
print(c)

'''  
   reason we use unpacking is swaping one value for another without 
   
   temporary value for storage   
   
'''

''' more examples of swapping '''

a, b = 23, 34
print(a, b)
print(id(a))
print(id(b))

b,a = a,b
print(a,b)
print(id(a))
print(id(b))

l = [23, 45,78]

a,b,c = l

print(a, b, c)

c,a = b,c

print(a, b, c)


''' unpacking set is not very useful'''

s = {'m', 'a','r','i'}

a,b,c,d = s

print(a,b,c,d)

''' unpacking dictionaries is not very useful 
        because order is not warranted
'''

d = {'a':23,'b':45,'c':56,'d':12}
print(d)
a,b,c,d = d
print(a,b,c,d)
print(d)

v = {'a':23,'b':45,'c':56,'d':12}

a,b,c,d = v.values()
print(a,b,c,d)

a,b,c,d = v.items()
print(a,b,c,d)











