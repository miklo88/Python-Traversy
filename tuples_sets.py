# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Mango', 'Pina', 'Naranja'))

# Single value needs trailing comma.
# fruits3 = ('Apples',) even with one value, use a trailing comma or it will be considered a string.

print(fruits, fruits2)
# fun
# print(fruits2[0])
# you cannot re-assign a value, a tuple is unchangeable
# fruits[0] = 'Pears'

# Delete tuple
del fruits

# Get length
print(len(fruits2))


# A Set is a collection which is unordered and unindexed. No duplicate members.
# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# Remove from set
fruits_set.remove('Grapes')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)
# returns set() so it doesn't delete it, just clears it. you technically still have your fruits set.

# Delete
# del fruits_set
# print(fruits_set)
# returns as undefined.
