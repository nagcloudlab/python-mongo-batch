
# Tuples in Python are very similar to lists, but they are immutable, 
# which means once a tuple is created, its contents cannot be modified. 
# Tuples are defined by enclosing the elements in parentheses () instead of square brackets [] used for lists. 
# Despite their simplicity, tuples are used extensively in Python for fixed data storage, returning multiple values from functions, and for places where an immutable sequence of objects is needed.


# Creating a Tuple
# You can create a tuple by placing all the items (elements) inside parentheses (),
# separated by commas, or by using the tuple() function.

# Example:
# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Create a tuple using the tuple() function
my_tuple = tuple([1, 2, 3, 4, 5])
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# without parantheses
my_tuple = 1, 2, 3, 4, 5
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# A single item tuple must have a trailing comma, otherwise it will be treated as a string.

# Example:
# Create a single item tuple
my_tuple = (1,)
print(my_tuple)  # Output: (1,)

# Accessing Tuple Items
# You can access tuple items by referring to the index number, inside square brackets [].

# Example:
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Modifying Tuple Items
# Tuples are immutable, meaning you cannot change, add, or remove items after the tuple is created.

# Example:
# my_tuple[1] = 20  # Output: TypeError: 'tuple' object does not support item assignment

# You can convert the tuple to a list, change the list, and convert the list back to a tuple.

# Example:
# Convert the tuple to a list
my_list = list(my_tuple)
# Change the list
my_list[1] = 20
# Convert the list back to a tuple
my_tuple = tuple(my_list)

# Looping Through a Tuple
# You can loop through the tuple items by using a for loop.

# Example:
for item in my_tuple:
    print(item)

# Tuple Length
# You can get the length of a tuple using the len() method.
    
# Example:
print(len(my_tuple))  # Output: 5

# Adding Items to a Tuple
# You cannot add items to a tuple. Tuples are immutable.

# Example:
# my_tuple.add(6)  # Output: AttributeError: 'tuple' object has no attribute 'add'

# Removing Items from a Tuple
# You cannot remove items from a tuple. Tuples are immutable.

# Example:
# my_tuple.remove(3)  # Output: AttributeError: 'tuple' object has no attribute 'remove'

# Deleting a Tuple
# You can delete the entire tuple using the del keyword.

# Example:
del my_tuple
# print(my_tuple)  # Output: NameError: name 'my_tuple' is not defined

# Joining Tuples
# You can join two or more tuples using the + operator.

# Example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2

print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)

# Multiplying Tuples
# You can multiply a tuple by an integer to create a new tuple.

# Example:
tuple1 = (1, 2, 3)
tuple2 = tuple1 * 3

print(tuple2)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# count() - Returns the number of times a specified value occurs in a tuple
# index() - Searches the tuple for a specified value and returns the position of where it was found

# Example:
my_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3)
print(my_tuple.count(1))  # Output: 3

print(my_tuple.index(3))  # Output: 2
print(my_tuple.index(3, 3))  # Output: 7
print(my_tuple.index(3, 6, 9))  # Output: 7

# Tuple Packing and Unpacking
# In tuple packing, the values are placed inside a tuple, and the tuple is assigned to a single variable.

# Example:
my_tuple = 1, 2, 3, 4, 5
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# In tuple unpacking, the values in a tuple are assigned to multiple variables.

# Example:
a, b, c, d, e = my_tuple
print(a)  # Output: 1

# You can also use the * operator to assign the rest of the values to a variable.

# Example:
a, *b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

# Using the * operator to assign the rest of the values to a variable is called extended unpacking.

# Tuple Comprehension
# Python does not support tuple comprehension.

# Tuple vs List
# The main difference between lists and tuples is the mutability.
# Lists are mutable, meaning you can change, add, and remove items after the list is created.
# Tuples are immutable, meaning you cannot change, add, or remove items after the tuple is created.



# Tuple slice

# Example:
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple[1:5])  # Output: (2, 3, 4, 5)



