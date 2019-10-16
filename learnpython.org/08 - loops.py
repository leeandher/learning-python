print('--- Running loops.py ---')

# For-loop syntax
primes = [2, 3, 5, 7, 11, 13]
out_prime = ""
for prime in primes:
    out_prime += "%s " % repr(prime)
print(out_prime)

# Using ranges
# range(start, stop, step), start is inclusive, stop is not
out_x = ""
for x in range(5):
    out_x += "%s " % repr(x)
print(out_x)

out_x = ""
for x in range(2, 7):
    out_x += "%s " % repr(x)
print(out_x)


out_x = ""
for x in range(3, 8, 2):
    out_x += "%s " % repr(x)
print(out_x)

# While-loop syntax
counter = 0
out_counter = ""
while counter < 10:
    out_counter += "%s " % counter
    counter += 1
print(out_counter)

# Using breaks and continues

counter = 0
out_counter = ""
while True:
    out_counter += "%s " % counter
    counter += 1
    if counter >= 15:
        break  # escape the loop if this condition is met

out_x = ""
for x in range(10):
    if x % 2 == 0:
        continue  # skip to the next iteration if this conditional is met
    out_x += "%s " % x
print(out_x)

# Python's fancy else-loop features
# else blocks are executed upon a loops completion, so long as the block

counter = 0
out_counter = ""
while counter < 5:
    out_counter += "%s " % counter
    counter += 1
else:
    print("The while loop is complete! - out_counter = %s" % out_counter)

for x in range(20):
    if x == 10:
        print("x has gotten to a value of %d, and now we break out." % x)
        break
else:
    print("This code will never run")

# Exercise
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

print("Starting numbers loop...")
out_numbers = ""
for i in range(len(numbers)):
    out_numbers += "%s " % repr(numbers[i])
    if (numbers[i] == 237):
        print(out_numbers)
        print("Found 237, breaking...")
        break

print('--- Finished loops.py ---')
