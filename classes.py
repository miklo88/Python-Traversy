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
    # Init user object
carl = User('Carlitos Redding', 'carlsemail@email.com', 31)

print(type(carl))
# accessing the properties of the object
print(carl.name)
print(carl.email)
print(carl.age)
carl.has_birthday()
print(carl.greeting())
