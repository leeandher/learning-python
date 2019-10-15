print('--- Running string_formatting.py ---')

# Formatting strings is done with a C-style interpolation method
name = "John"
print("Hey there %s!" % name)

# Specifying multiple variables
age = 23
print("%s is only %d years old!" % (name, age))

# Using lists
my_list = [1, 2, 3, 4]
print("Printing a list: %s" % my_list)


# NOTE
# %s - String, or any object with a string representation
# %d - Integers
# %f - Floating point numbers
# %.xf - Floating point numbers where x represents decimal places
# %x/%X - Integers in hex representation (using either lowercase/uppercase respectively)

# Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)

print('--- Finished string_formatting.py ---')
