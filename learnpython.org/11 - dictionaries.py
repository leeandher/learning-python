print('--- Running dictionaries.py ---')

# Dictionaries work a lot like JS objects
phonebook = {
    "John": 1234567890,
    "Jack": 1234567891
}
phonebook["Jacob"] = 1234567892
phonebook["Jessica"] = 1234567893
print(phonebook["Jack"])
print(phonebook["Jacob"])
print(phonebook)

# You can use different data-types for saving entries to the dictionary
phonebook[1] = "Jamothy"
print(phonebook[1])

# Deleting them is done as follows
del phonebook[1]
print(phonebook)
# or...
phonebook[1] = "Jamothy"
phonebook.pop(1)
print(phonebook)

# To iterate over dictionaries...
for name, number in phonebook.items():
    print("Phone Number of %s is %d" % (name, number))

# Exercise
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


print('--- Finished dictionaries.py ---')
