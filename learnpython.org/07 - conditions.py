print('--- Running conditions.py ---')

# Basics
x = 2
print(x == 2)  # True
print(x == 3)  # False
print(x < 3)  # True


# Using booleans in conditionals
name = "John"
age = 23
if name == "John" and age == 23:
    print("John is 23!")
if name == "John" or name == "Rick":
    print("The name is either John or Rick")

# in Operator for iterables
if name in ["Jacob", "Ryan"]:
    print("The name was found!")
else:
    print("The name wasn't found")

# is Operator for checking statements/variables
x = 2
y = 2
print(x is y)  # Value-checking for primitives - True
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Instance-checking for objects - False
y = x
print(x is y)  # True
print((len(x) < 4) is True)  # Conditional checking, unnecessary

# not Operator for inverting conditionals
print(not True)  # False
print(not len(x) != 3)  # True

# Exercise
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

print('--- Finished conditions.py ---')
