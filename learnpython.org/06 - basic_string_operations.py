print('--- Running basic_string_operations.py ---')

str = "Hello world!"

# Getting the length of a string
print(len(str))  # 12

# Getting the first appearance of 'o'
print(str.index('o'))  # 4

# Counting the number of 'l's
print(str.count('l'))  # 3

# Slicing a string -> [start : stop : step]
# start is included, stop is excluded
print(str[3:7])  # lo_w
print(str[2:9:2])  # lowr
print(str[3:7:2])  # l_

# Reversing a string
print(str[::-1])

# Formatting the strings
print(str.upper())
print(str.lower())

# Checking contents of the string
print(str.startswith("Hello"))  # True
print(str.endswith("World!"))  # False

# Converting to a list
print(str.split(' '))
print(str.split('l'))

# Exercise
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

print('--- Finished basic_string_operations.py ---')
