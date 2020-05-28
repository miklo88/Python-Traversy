# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
- Variable names are case sensitive (name and NAME are different variables)
- Must start with a letter or an underscore
- Can have numbers but can not start with one
"""

# Main types you will be dealing with

# # int
# x = 1
# # float
# y = 2.5
# # string
# name = 'John'
# # bool
# is_cool = True

# Multiple assignment
x, y, name, is_cool, = (1, 2.5, 'John', True)

# print() is an output function in python like console.log in javascript
# print('Hola!')
print(x, y, name, is_cool)

# Basic math
a = x + y

# print(x, y, name, is_cool)
# print(a)

# type function to give us the type of int. output in term should be
# <class 'int'>
# print(type(x))
# thius is where we want to cast a different type of value to x aka casting
# #casting
x = str(x)
y = int(y)
z = float(y)
# print(type(x))
#  output is <class 'str'>
print(type(y), y)
#  output is <class 'int'> 2
print(type(z), z)
#  output is <class 'float'> 2.0
