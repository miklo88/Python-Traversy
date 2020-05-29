# Python has functions for creating, reading, updating and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')
# created a myfile.txt file

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ',myFile.mode)

# Write to file
myFile.write('I love cafecito cubano,')
myFile.write(' also Python and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like Grokking Algorithms')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)