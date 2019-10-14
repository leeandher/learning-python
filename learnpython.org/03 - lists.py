print('--- Running lists.py ---')

# Interacting with lists
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])

# Throwing an error if it's out of range
try:
    print(my_list[10])
except IndexError:
    print("You can't query indexes out of range")

# Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print('--- Finished lists.py ---')
