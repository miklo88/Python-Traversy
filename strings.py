# working on inserting variables into strings and formatting
# String formatting and some string methods
# all strings have methods attatched to them.

name = 'Carlitos'
age = 31
# concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))
# # output Hello, my name is Carlitos and I am 31

# F-Strings available in python 3.6 and later
print(f'Hola my name is {name} and I am {age}')

# String Formatting

# Arguments by position
# within the format() method we have placeholders name and age. when invoked the should show up in our string.
print('My name is {name} and I am {age}'.format(name=name, age=age))

# String Methods
s = 'hello world'
# Capitalize string
print(s.capitalize())
# Make all uppercase
print(s.upper())
# Make all lowercase
print(s.lower())
# Swap case
print(s.swapcase())
# Get length ## can be used on strings, lists, any data type
print(len(s))
# Replace takes world and replaces with everyone
print(s.replace('world', 'everyone'))
# Count - counts num of h's in string
sub = 'h'
print(s.count(sub))
# Starts with # returns true or false
print(s.startswith('hello'))
# Ends with # same as starts
print(s.endswith('d'))
# Split into a list # take string and turn into list which is basically an array
# Find position
print(s.find('r'))
# Is all alphanumeric
print(s.isalnum())
# Is all alphabetic
print(s.isalpha())
# Is all numeric
print(s.isnumeric())


# goofin
feet = 5
inches = 7

print('My height is {feet} foot {inches}'.format(feet=feet, inches=inches))
