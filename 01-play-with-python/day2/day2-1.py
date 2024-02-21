
# every thing in python is object


# 1.int
# 2.float
# 3.bool
# 4.str

# x=12
# print(type(x))
# print(isinstance(x, int))
# print(x.bit_length())



x=12
y=12.0
z=True
a="hello"

# -----------------------------

# 5.list

# Creating a list

my_list = [1, 2, 3, 4, 5]
print(my_list) # output: [1, 2, 3, 4, 5]

my_list = list(range(1, 6))
print(my_list) # output: [1, 2, 3, 4, 5]

# length of list
print(len(my_list)) # output: 5

# Accessing elements of list
print(my_list[0]) # output: 1
print(my_list[1]) # output: 2

# Modify elements of list
my_list[0] = 100
print(my_list) # output: [100, 2, 3, 4, 5]

# Add elements to list
# You can add items to the end of a list using the append() method:
my_list.append(200)
print(my_list) # output: [100, 2, 3, 4, 5, 200]

# You can add items at a specific index by using the insert() method:
my_list.insert(2, 300)
print(my_list) # output: [100, 2, 300, 3, 4, 5, 200]

# Removing Items from a List
# You can remove items from the list using the remove() method:
my_list.remove(300)
print(my_list) # output: [100, 2, 3, 4, 5, 200]

# You can remove items from the list using the pop() method:
my_list.pop()
print(my_list) # output: [100, 2, 3, 4, 5]

# You can remove items from the list using the del keyword:
del my_list[0]
print(my_list) # output: [2, 3, 4, 5]

# You can remove all items from the list using the clear() method:
my_list.clear()
print(my_list) # output: []


# Looping Through a List
# You can loop through a list using a for loop:
my_list = [1, 2, 3, 4, 5]
for x in my_list:
  print(x)

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if 1 in my_list:
  print("Yes, '1' is in the list")


# List Comprehension
# List comprehension offers a shorter syntax 
# when you want to create a new list based on the values of an existing list.
  
# Without list comprehension
my_list = [1, 2, 3, 4, 5]

new_list = []
for x in my_list:
  if x > 2:
    new_list.append(x)

print(new_list) # output: [3, 4, 5]


# With list comprehension
my_list = [1, 2, 3, 4, 5]

new_list = [x for x in my_list if x > 2]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']

# The syntax is [expression for item in iterable if condition == True].
# The return value is a new list, leaving the old list unchanged.
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
# The iterable can be any iterable object, like a list, tuple, set etc.
# The condition is like a filter that only accepts the items that evaluate to True.
# The condition is optional and can be omitted.


# More Examples:

# Example 1
# Convert all the characters in a string to upper case using list comprehension.

# Without list comprehension
string = "hello"
new_string = []
for char in string:
  new_string.append(char.upper())

print(new_string) # output: ['H', 'E', 'L', 'L', 'O']

# With list comprehension
string = "hello"
new_string = [char.upper() for char in string if char != "l"]
print(new_string) # output: ['H', 'E', 'O']


# Create a new list with only the even numbers from the original list:
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x for x in original_list if x % 2 == 0]
print(new_list)  # Output: [2, 4, 6, 8, 10]

# Create a new list with only the positive numbers from the original list:
original_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
new_list = [x for x in original_list if x > 0]


# Example:
# Return "Hello" if the number is less than 5, otherwise return "World":
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = ["Hello" if x < 5 else "World" for x in original_list]
print(new_list)  # Output: ['Hello', 'Hello', 'Hello', 'Hello', 'World', 'World', 'World', 'World', 'World', 'World']


# Replace negative numbers with the string "Negative":
original_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
new_list = [x if x > 0 else "Negative" for x in original_list]
print(new_list)  # Output: [1, 'Negative', 3, 'Negative', 5, 'Negative', 7, 'Negative', 9, 'Negative']



# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
thatlist = thislist

thatlist.append("orange")
print(thatlist)  # Output: ['apple', 'banana', 'cherry', 'orange']
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orange']

# To make a copy, use the built-in method copy():
thislist = ["apple", "banana", "cherry"]
thatlist = thislist.copy()

thatlist.append("orange")
print(thatlist)  # Output: ['apple', 'banana', 'cherry', 'orange']
print(thislist)  # Output: ['apple', 'banana', 'cherry']


# extend

# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# index

# What is the position of the value "cherry":
thislist = ["apple", "banana", "cherry"]
x = thislist.index("cherry")
print(x)  # Output: 2


# sort

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  # Output: [23, 50, 65, 82, 100]

# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)  # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


# List slice

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

# Example
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Output: ['cherry', 'orange', 'kiwi']

# By leaving out the start value, the range will start at the first item:
print(thislist[:4])  # Output: ['apple', 'banana', 'cherry', 'orange']

# By leaving out the end value, the range will go on to the end of the list:
print(thislist[2:])  # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Negative Indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

# Example
# This example returns the items from "orange" and to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:])  # Output: ['orange', 'kiwi', 'melon', 'mango']

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

# Example
# This example returns the items from "cherry" to, but NOT including "mango":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-5:-2])  # Output: ['cherry', 'orange', 'kiwi']


list=[1,2,3,4,5]
print(list[0::2]) # Output: [1, 3, 5]
print(list[1::2]) # Output: [2, 4]



# List Concatenation
# You can concatenate two or more lists using the + operator.

# Example
# Concatenate two lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]

# List Repetition
# You can use the * operator to repeat a list.

# Example
# Repeat a list:
list1 = ["a", "b", "c"]
list2 = list1 * 2
print(list2)  # Output: ['a', 'b', 'c', 'a', 'b', 'c']


list=None
print(list) # Output: None

list=[]
print(list) # Output: []


# how to find index of element in list ?

list=[1,2,3,4,5]
print(list.index(3)) # Output: 2


# --------------------------------

# 6.tuple

# list vs tuple
# 1. list is mutable, tuple is immutable
# 2. list is created using [], tuple is created using ()
# 3. list is slower than tuple


# When to use tuple over list?

# 1. If you have a collection of values that will not change, use a tuple because it is immutable.
# 2. If you have a collection of values that may change, use a list because it is mutable.


# Tuples in Python are very similar to lists, but they are immutable, 
# which means once a tuple is created, its contents cannot be modified. 
# Tuples are defined by enclosing the elements in parentheses () instead of square brackets [] used for lists. 
# Despite their simplicity, tuples are used extensively in Python for fixed data storage, returning multiple values from functions, and for places where an immutable sequence of objects is needed.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) # output: (1, 2, 3, 4, 5)

my_tuple = tuple([1,2,3,4,5])
print(my_tuple) # output: (1, 2, 3, 4, 5)

# Without the parentheses, the comma is treated as an operator,
# and connects the two values into a tuple.
my_tuple = 1, 2, 3, 4, 5
print(my_tuple) # output: (1, 2, 3, 4, 5)

# A single item tuple must have a trailing comma, otherwise it will be treated as a string.
single_element_tuple = ("1",)
print(type(single_element_tuple))

# Accessing elements of tuple
print(my_tuple[0]) # output: 1
print(my_tuple[1]) # output: 2


# Modify elements of tuple
# my_tuple[0] = 100 # output: TypeError: 'tuple' object does not support item assignment


# Add elements to tuple

# You cannot add items to a tuple. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, add the item, and convert the list back into a tuple.

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
my_list.append("orange")
my_tuple = tuple(my_list)

print(my_tuple) # output: ('apple', 'banana', 'cherry', 'orange')

# Looping Through a Tuple
# You can loop through a tuple using a for loop:

my_tuple = ("apple", "banana", "cherry")
for x in my_tuple:
  print(x)

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
if "apple" in my_tuple:
  print("Yes, 'apple' is in the tuple")


# Tuple Methods
# Python has two built-in methods that you can use on tuples.
  
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


# count
# Return the number of times the value 5 appears in the tuple:
my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = my_tuple.count(5)
print(x)  # Output: 2

# index
# Search for the first occurrence of the value 8, and return its position:
my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = my_tuple.index(8)
print(x)  # Output: 3


# Tuple Concatenation
# You can concatenate two or more tuples using the + operator.

# Example
# Concatenate two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)

# Tuple Repetition
# You can use the * operator to repeat a tuple.

# Example
# Repeat a tuple:
tuple1 = ("a", "b" , "c")
tuple1 = tuple1 * 2

print(tuple1)  # Output: ('a', 'b', 'c', 'a', 'b', 'c')


# Tuple Slicing
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.

# Example
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Output: ('cherry', 'orange', 'kiwi')


# Deleting tuple
# Tuples are immutable, so you can not remove elements from it, but you can delete the tuple completely.

# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple



# Tuple Packing and Unpacking

my_tuple = 3, 4.6, "dog"  
print(my_tuple)  # Output: (3, 4.6, 'dog')

# This is called tuple packing.

# Unpacking a tuple
a, b, c = my_tuple
print(a)  # Output: 3
print(b)  # Output: 4.6
print(c)  # Output: dog



my_tuple = 1, 2, 3, 4, 5
a, *b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5


# Tuple Comprehension

# Tuple comprehension is not supported in python.
# You can use generator expression to create tuple.

# Example
# Create a tuple with the numbers 0 to 9:
my_tuple = tuple(i for i in range(10))
print(my_tuple)  # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# --------------------------------

# Summary

# -> use list when you have a collection of values that may change
# -> use tuple when you have a collection of values that will not change

# --------------------------------

def getValues():
  return 1, 2, 3 # packing

a, b, c = getValues() # unpacking

#--------------------------------

# 7.set

# to hold unique values
# set is mutable
# set is unordered
# set is created using {}


# Python sets are collections that are unordered, mutable, and do not allow duplicate elements. 
# They are useful when you need to ensure the uniqueness of the items, 
# perform set operations like unions, intersections, differences, or simply check for the membership of elements efficiently. 
# Here's an overview of some of the most common set methods in Python:


# Creating a Set
# You can create a set by placing all the items (elements) inside curly braces {}, 
# separated by commas, or by using the set() function.

# Example
# Create a set:
my_set = {1, 2, 3, 4, 5}
print(my_set) # output: {1, 2, 3, 4, 5}
print(type(my_set)) # output: <class 'set'>

my_set = set([1, 2, 3, 4, 5])
print(my_set) # output: {1, 2, 3, 4, 5}

# Note: You cannot create an empty set using {}, you have to use set().
my_set = set()

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,2,3,4,5,6,7,8,9,10}
print(my_set) # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Accessing Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Example
# Loop through the set, and print the values:
my_set = {1, 2, 3, 4, 5}
for x in my_set:
  print(x)

# Check if "banana" is present in the set:
my_set = {"apple", "banana", "cherry"}

print("banana" in my_set) # output: True

# Add Items

# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.

# Example
# Add an item to a set, using the add() method:
my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # output: {1, 2, 3, 4}

# Add multiple items to a set, using the update() method:
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set) # output: {1, 2, 3, 4, 5, 6}

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# Example
# Remove "banana" by using the remove() method:
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set) # output: {'apple', 'cherry'}

# If the item to remove does not exist, remove() will raise an error.

# Example
# Remove "banana" by using the discard() method:
my_set = {"apple", "banana", "cherry"}
my_set.discard("banana")    
print(my_set) # output: {'apple', 'cherry'}

# If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.

# Example
# Remove the last item by using the pop() method:
my_set = {"apple", "banana", "cherry"}
print(my_set) # output: {'apple', 'banana', 'cherry'}
x = my_set.pop()
print(x) # output: apple


# The clear() method empties the set:

# Example
# Remove all items in the set by using the clear() method:
my_set = {"apple", "banana", "cherry"}
my_set.clear()

print(my_set) # output: set()

# The del keyword will delete the set completely:

# Example
# Delete the set completely:
my_set = {"apple", "banana", "cherry"}
del my_set

# print(my_set) # output: NameError: name 'my_set' is not defined


# Set Comprehension
# Set comprehension offers a shorter syntax when you want to create a new set based on the values of an existing set.


# Example:
# Create a new set based on the values of an existing set
fruits = {"apple", "banana", "cherry", "kiwi", "mango"}
new_set = {x for x in fruits if "a" in x}
print(new_set)  # Output: {'mango', 'banana', 'apple'}

# The syntax is {expression for item in iterable if condition == True}.
# The return value is a new set, leaving the old set unchanged.


# Set Operations
# You can perform various set operations like union, intersection, difference, and symmetric difference using the following methods:


# union() - Returns a new set containing all the items from both sets.
# intersection() - Returns a new set containing the items that are present in both sets.
# difference() - Returns a new set containing the items that are present in the first set but not in the second set.
# symmetric_difference() - Returns a new set containing the items that are present in only one of the sets.


# Example
# Perform set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# intersection
print(set1.intersection(set2))  # Output: {4, 5}

# difference
print(set1.difference(set2))  # Output: {1, 2, 3}

# symmetric_difference
print(set1.symmetric_difference(set2))  # Output: {1, 2, 3, 6, 7, 8}





# You can also use the following methods to perform set operations:

# update() - Updates the set with the union of itself and another set.
# intersection_update() - Updates the set with the intersection of itself and another set.
# difference_update() - Updates the set with the difference of itself and another set.
# symmetric_difference_update() - Updates the set with the symmetric difference of itself and another set.


# Example
# Perform set operations using update() method
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# update
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set2)  # Output: {4, 5, 6, 7, 8}

# intersection_update
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1.intersection_update(set2)
print(set1)  # Output: {4, 5}
print(set2)  # Output: {4, 5, 6, 7, 8}

# difference_update
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1.difference_update(set2)
print(set1)  # Output: {1, 2, 3}
print(set2)  # Output: {4, 5, 6, 7, 8}

# symmetric_difference_update
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 3, 6, 7, 8}
print(set2)  # Output: {4, 5, 6, 7, 8}



# Set Methods
# Here's a list of some of the most common set methods in Python:

# add() - Adds an element to the set.
# clear() - Removes all the elements from the set.
# copy() - Returns a copy of the set.
# difference() - Returns a set containing the difference between two or more sets.
# difference_update() - Removes the items in this set that are also included in another, specified set.
# discard() - Remove the specified item.
# intersection() - Returns a set, that is the intersection of two other sets.
# intersection_update() - Removes the items in this set that are not present in other, specified set(s).
# isdisjoint() - Returns whether two sets have a intersection or not.
# issubset() - Returns whether another set contains this set or not.
# issuperset() - Returns whether this set contains another set or not.
# pop() - Removes an element from the set.
# remove() - Removes the specified element.
# symmetric_difference() - Returns a set with the symmetric differences of two sets.
# symmetric_difference_update() - inserts the symmetric differences from this set and another.
# union() - Return a set containing the union of sets.
# update() - Update the set with the union of this set and others.


# --------------------------------

# list -> index based & ordered & mutable
# tuple -> index based & ordered & immutable
# set -> unordered & mutable & unique values

# --------------------------------

# 8.dict


# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

# Example
# Create and print a dictionary:
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(my_dict) # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example
# Get the value of the "model" key:
x = my_dict["model"]
print(x) # output: Mustang

# There is also a method called get() that will give you the same result:

# Example
# Get the value of the "model" key:
x = my_dict.get("model")
print(x) # output: Mustang

# Change Values
# You can change the value of a specific item by referring to its key name:

# Example
# Change the "year" to 2018:
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict["year"] = 2018


# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.

# Example
# Print all key names in the dictionary, one by one:
for x in my_dict:
  print(x)

# Example
# Print all values in the dictionary, one by one:
for x in my_dict:
  print(my_dict[x])

# You can also use the values() method to return values of a dictionary:
  
# Example
# Print all values in the dictionary, one by one:
for x in my_dict.values():
  print(x)

# Example
# Loop through both keys and values, by using the items() method:
for x, y in my_dict.items():
  print(x, y)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
  
# Example
# Check if "model" is present in the dictionary:
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in my_dict:
    print("Yes, 'model' is one of the keys in the my_dict dictionary")


# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() method.
    
# Example
# Print the number of items in the dictionary:
print(len(my_dict)) # output: 3


# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# Example
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

my_dict["color"] = "red"

print(my_dict) # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Removing Items

# There are several methods to remove items from a dictionary:

# Example
# The pop() method removes the item with the specified key name:
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

my_dict.pop("model")
print(my_dict) # output: {'brand': 'Ford', 'year': 1964}

# -----------------------------

# data types in python

# simple types

# 1.int
# 2.float
# 3.bool
# 4.str

# complex types

# 5.list
# 6.tuple
# 7.set
# 8.dict

# -----------------------------

# operators
# conditional statements
# loops

# -----------------------------







