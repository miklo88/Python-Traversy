# A function is a block of code which only runs when it is called. In python, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hola {name}')


sayHello('Carlitos')


# can also invoke function with no argument
def sayHello(name='Muchachicho'):
    print(f'Hola {name}')


sayHello()


# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


# most of the time you'll be assigning it to a variable
num = getSum(3, 14)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
#   implicitly returns
getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 17))