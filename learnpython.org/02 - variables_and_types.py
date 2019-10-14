print('--- Running variables_and_types.py ---')

# Using integer variables
my_int = 14
print(my_int)

# Using float variables
my_float1 = 14.56
print(my_float1)
my_float2 = float(14)
print(my_float2)

# Using string variables
my_string = 'hello'
print(my_string)
my_string = "hello_modified"
print(my_string)

# Using simple operators
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = 'world'
statement = hello + ' ' + world
print(statement)

# Simulatenous declarations
a, b = 1, 2
print(a, b)

# Mixing operators does not work
try:
    print(hello + one + world)
except TypeError:
    print("The above statement didn't work!")

# Exercise
my_string = 'hello'
my_float = 10.0
my_int = 20

# Testing the code
if my_string == "hello":
    print("String: %s" % my_string)
if isinstance(my_float, float) and my_float == 10.0:
    print("Float: %f" % my_float)
if isinstance(my_int, int) and my_int == 20:
    print("Integer: %d" % my_int)


print('--- Finished variables_and_types.py ---')
