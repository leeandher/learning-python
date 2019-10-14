print('--- Running basic_operators.py ---')

# Arithmetic Operators -> *, then /, then + (BEDMAS)
number = 1 + 2 * 3 / 4.0
print(number)

# Using remainders
remainder = 11 % 3
print(remainder)

# Using exponents
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# Operating with strings
statement = "hello" + ' ' + "world"
print(statement)
ten_hellos = "hello" * 10
print(ten_hellos)

# Operating with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
lots_of_even_numbers = even_numbers * 3
print(lots_of_even_numbers)

# Exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

print('--- Finished basic_operators.py ---')
