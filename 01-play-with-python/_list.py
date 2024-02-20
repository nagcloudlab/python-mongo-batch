
# Python lists are versatile containers that allow you to store a sequence of items. 
# These items can be of any type, and a single list can even contain items of different types 
# (though it's more common for items to be of the same type). 
# Lists are mutable, meaning you can modify them after their creation. 



# Creating a List
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# List Length
# To find out how many items a list has, use the len() function:
print(len(my_list))  # Output: 5

# Accessing List Items
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3


# Modifying List Items
my_list[1] = 20
print(my_list)  # Output: [1, 20, 3, 4, 5]

# Adding Items to a List

# You can add items to the end of a list using the append() method:
my_list.append(6)
print(my_list)  # Output: [1, 20, 3, 4, 5, 6]

# You can also add items at a specific index using the insert() method:
my_list.insert(1, 10)
print(my_list)  # Output: [1, 10, 20, 3, 4, 5, 6]

# Removing Items from a List
# You can remove items from a list using the remove() method:
my_list.remove(10)

# You can also remove items at a specific index using the pop() method:
my_list.pop(2)

# You can also remove items at a specific index using the del statement:
del my_list[0]

# You can also remove all items from a list using the clear() method:
my_list.clear()

# Looping Through a List
# You can loop through a list using a for loop:

for item in my_list:
    print(item)

# List Comprehension
    
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

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
# Create a new list with only the even numbers from the original list:
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x for x in original_list if x % 2 == 0]
print(new_list)  # Output: [2, 4, 6, 8, 10]

# Example 2
# Create a new list with only the positive numbers from the original list:
original_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
new_list = [x for x in original_list if x > 0]

# Example 3
# Create a new list with only the odd numbers from the original list:
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x for x in original_list if x % 2 != 0]

# Example 4
# Create a new list with only the numbers greater than 5 from the original list:
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x for x in original_list if x > 5]

# With If Else
# You can also use the else keyword on the output expression.

# Example:
# Return "Hello" if the number is less than 5, otherwise return "World":
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = ["Hello" if x < 5 else "World" for x in original_list]

# Example 2
# Replace negative numbers with the string "Negative":
original_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
new_list = [x if x > 0 else "Negative" for x in original_list]


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


# copy() method
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().
# Example:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# Another way to make a copy is to use the built-in method list().
# Example:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# extend() method
# Add elements of a list to another list
# Example:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]

# index() method
# Returns the index of the first element with the specified value
# Example:
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)  # Output: 2

# insert() method
# Adds an element at the specified position
# Example:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

# pop() method
# Removes the element at the specified position
# Example:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

# remove() method
# Removes the first item with the specified value
# Example:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

# reverse() method
# Reverses the order of the list
# Example:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

# sort() method
# Sorts the list
# Example:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

# List Slice

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

# Example:
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])  # Output: ['cherry', 'orange', 'kiwi']

# By leaving out the start value, the range will start at the first item:
print(thislist[:4])  # Output: ['apple', 'banana', 'cherry', 'orange']

# By leaving out the end value, the range will go on to the end of the list:
print(thislist[2:])  # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Example:

print(thislist[-1])  # Output: mango
print(thislist[-4:-1])  # Output: ['orange', 'kiwi', 'melon']

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Example:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")  # Output: Yes, 'apple' is in the fruits list

# List Concatenation
# To add two lists together, you can use the + operator:
# Example:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]

# List Repetition
# To repeat a list, you can use the * operator:
# Example:
list1 = ["a", "b", "c"]
list2 = list1 * 2
print(list2)  # Output: ['a', 'b', 'c', 'a', 'b', 'c']

# List Membership Test
# You can test if an item is in a list using the in keyword:
# Example:
list1 = ["a", "b", "c"]
if "a" in list1:
    print("Yes, 'a' is in the list")  # Output: Yes, 'a' is in the list

# List Iteration
# You can iterate through a list using a for loop:
# Example:
list1 = ["a", "b", "c"]
for x in list1:
    print(x)

# List Length
# To determine how many items a list has, use the len() function:
# Example:
list1 = ["a", "b", "c"]
print(len(list1))  # Output: 3

# List Sort
# You can sort a list using the sort() method:
# Example:
list1 = ["c", "b", "a"]
list1.sort()

# More Advanced List Operations

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']




