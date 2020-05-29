# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# similair to an object literal in JavaScript

# Create a Dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person, type(person))

# can use a constructor
person2 = dict(first_name='Leonardo', last_name='DaVinci')

# Get Value # in javascript you'd use person.first_name aqui you use brackets
print(person['first_name'])
print(person2['first_name'])
# using get method, more common way
print(person.get('last_name'))
print(person2.get('last_name'))

# Add key/value
person['phone'] = '239-867-5309'

# Get dictionary keys
print(person.keys())


# Get dictionary items
print(person.items())

# Copy a dictionary
person3 = person.copy()
# similair to a spread operator
person3['city'] = 'Miami'

print(person3)

# Remove an item
del(person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()

# Get length
print(len(person2))

# List of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Maria', 'age': 25},
]
print(people)
# grabbing name of specific person
print(people[0]['name'])
