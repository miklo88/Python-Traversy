# A list is a collection which is ordered and changeable. Allows duplicate members.

# Create list / more common way of doing so.
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Kiwis', 'Bananas', 'Mangos', 'Grapes']
# use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Guayava')

# Remove from list
fruits.remove('Grapes')

# insert into position number is position number, strawberries is what to insert
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse the list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
