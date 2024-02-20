

# Python sets are collections that are unordered, mutable, and do not allow duplicate elements. 
# They are useful when you need to ensure the uniqueness of the items, 
# perform set operations like unions, intersections, differences, or simply check for the membership of elements efficiently. 
# Here's an overview of some of the most common set methods in Python:

# Creating a Set
# You can create a set by placing all the items (elements) inside curly braces {}, 
# separated by commas, or by using the set() function.

# Example:
# Create a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Create a set using the set() function
my_set = set([1, 2, 3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding Items to a Set
# You can add items to a set using the add() method.

# Example:
# Add an item to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# You can also add multiple items to a set using the update() method.

# Example:
# Add multiple items to a set
my_set.update([7, 8, 9])

# You can also add items from another set to the current set using the update() method.

# Example:
# Add items from another set to the current set
my_set.update({10, 11, 12})

# Removing Items from a Set
# You can remove items from a set using the remove() method.

# Example:
# Remove an item from a set
my_set.remove(1)

# You can also remove an item from a set using the discard() method.

# Example:
# Remove an item from a set using the discard() method
my_set.discard(2)

# You can also remove an item from a set using the pop() method.

# Example:
# Remove an item from a set using the pop() method
my_set.pop()

# revove vs discard vs pop
# The remove() method raises an error if the item to be removed is not in the set,
# while the discard() method does not raise an error if the item to be removed is not in the set.
# The pop() method removes and returns an arbitrary item from the set.

# You can also remove all items from a set using the clear() method.

# Example:
# Remove all items from a set
my_set.clear()

# Looping Through a Set
# You can loop through a set using a for loop.

# Example:
# Loop through a set

my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

# Set Comprehension
# Set comprehension offers a shorter syntax when you want to create a new set based on the values of an existing set.
    
# Example:
# Create a new set based on the values of an existing set
fruits = {"apple", "banana", "cherry", "kiwi", "mango"}
new_set = {x for x in fruits if "a" in x}
print(new_set)  # Output: {'banana', 'mango', 'apple'}

# The syntax is {expression for item in iterable if condition == True}.

# Set Operations
# You can perform various set operations like union, intersection, difference, and symmetric difference using the following methods:

# union() - Returns a new set containing all the items from both sets.
# intersection() - Returns a new set containing the items that are present in both sets.
# difference() - Returns a new set containing the items that are present in the first set but not in the second set.
# symmetric_difference() - Returns a new set containing the items that are present in only one of the sets.

# Example:
# Perform set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
print(set1.intersection(set2))  # Output: {4, 5}

# Difference
print(set1.difference(set2))  # Output: {1, 2, 3}

# Symmetric Difference
print(set1.symmetric_difference(set2))  # Output: {1, 2, 3, 6, 7, 8}

# You can also use the following methods to perform set operations:

# update() - Updates the set with the union of itself and another set.
# intersection_update() - Updates the set with the intersection of itself and another set.
# difference_update() - Updates the set with the difference of itself and another set.
# symmetric_difference_update() - Updates the set with the symmetric difference of itself and another set.

# Example:
# Perform set operations using the update() method
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Perform set operations using the intersection_update() method
set1.intersection_update(set2)
print(set1)  # Output: {4, 5}

# Perform set operations using the difference_update() method
set1.difference_update(set2)    
print(set1)  # Output: set()

# Perform set operations using the symmetric_difference_update() method
set1.symmetric_difference_update(set2)
print(set1)  # Output: {4, 5, 6, 7, 8}

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


