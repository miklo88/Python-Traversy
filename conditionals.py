# If/ Else conditionals are used to decide to do something based on something being true of false
# x = 10
# y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# # Simple if
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# # Nested if
# if x > 2:
#     if x <= 10: 
#         print(f'{x} is greater than 2 and less than or equal to 10')

# Logical Operators (and, or, not) - Used to combine conditional statements
# and
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less than or equal to 10')
# # or
# if x > 2 or x <= 10:
#     print(f'{x} is greater than 2 or less than or equal to 10') 
# # not
# if not(x == y):
#     print(f'{x} is not equal to {y}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
x = 13
y = 20

numbers = [1,2,3,4,5,6,7,8,9,10]

# # in
# if x in numbers:
#     print(x in numbers)
    #  returns True, if not in numbers no output

# # not in
# if x not in numbers:
#     print(x not in numbers)
    # if x = 13 then this would be True. If x is in the numbers then no output

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
x = 20
y = 20

# is 
if x is y:
    print(x is y)

    # is not 
if x is y:
    print(x is not y)
    

    