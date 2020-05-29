# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python is an object.

# Create class
class User:
    #constructor a function that runs when you instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extend a class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My llamo es {self.name} y yo soy {self.age} y mi {self.balance}'

    # Init user object
carl = User('Carlitos Redding', 'carlsemail@email.com', 31)
# init customer object
celia = Customer('Celia Cruz', 'celia@azucar.com', 77)

print(type(carl))
# accessing the properties of the object
print(carl.name)
print(carl.email)
print(carl.age)
carl.has_birthday()
print(carl.greeting())

celia.set_balance(1000000)
print(celia.greeting())