#1
# 1. Create a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

# 2. Create a tuple with different data types
mixed_tuple = (10, "Hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)



# 3. Create a tuple with numbers and print one item
num_tuple = (10, 20, 30, 40, 50)
print(num_tuple[2])  # Prints the third item

# 4. Unpack a tuple into several variables
a, b, c, d, e = num_tuple
print(a, b, c, d, e)

# 5. Add an item to a tuple
num_tuple += (60,)  # Tuples are immutable, so we create a new one
print(num_tuple)

# 6. Convert a tuple to a string
string_tuple = ('H', 'e', 'l', 'l', 'o')
print(''.join(string_tuple))

# 7. Get the 4th element and the 4th from the last
print(num_tuple[3])  # 4th element
print(num_tuple[-4]) # 4th from last

# 8. Create the colon of a tuple (unclear requirement, assuming slicing)
print(num_tuple[:])  # Full copy of tuple

# 9. Find repeated items in a tuple
repeat_tuple = (1, 2, 3, 2, 4, 5, 3, 2)
print({item for item in repeat_tuple if repeat_tuple.count(item) > 1})

# 10. Check whether an element exists within a tuple
print(3 in repeat_tuple)  # True

# 11. Convert a list to a tuple
sample_list = [10, 20, 30]
sample_tuple = tuple(sample_list)
print(sample_tuple)

# 12. Remove an item from a tuple
new_tuple = tuple(x for x in num_tuple if x != 30)
print(new_tuple)

# 13. Slice a tuple
print(num_tuple[1:4])  # Slices from index 1 to 3

# 14. Find the index of an item in a tuple
print(num_tuple.index(20))  # Finds index of 20

# 15. Find the length of a tuple
print(len(num_tuple))

