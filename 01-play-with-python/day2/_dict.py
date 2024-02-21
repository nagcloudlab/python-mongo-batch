

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

# Example:
# Create a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets [].

# Example:
# Get the value of the "name" key
print(my_dict["name"])  # Output: John

# You can also use the get() method to access the items of a dictionary.

# Example:
# Get the value of the "age" key using the get() method
print(my_dict.get("age"))  # Output: 30

# Change Values
# You can change the value of a specific item by referring to its key name.

# Example:
# Change the "age" to 40
my_dict["age"] = 40

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# Example:
# Print all key names in the dictionary, one by one

for key in my_dict:
    print(key)

# Example:
# Print all values in the dictionary, one by one
for value in my_dict:
    print(my_dict[value])

# Example:
# You can also use the values() method to return values of a dictionary.
    
for value in my_dict.values():
    print(value)

# Example:
# Loop through both keys and values, by using the items() method.
for key, value in my_dict.items():
    print(key, value)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword.
    
# Example:
# Check if "name" is present in the dictionary
if "name" in my_dict:
    print("Yes, 'name' is one of the keys in the my_dict dictionary")

# Adding Items
# You can add an item to a dictionary by using a new index key and assigning a value to it.
    
# Example:
# Add a new item to the dictionary
my_dict["email"] = "foo@mail.com"


# -------------------------------------------------------------------

# Creating a Dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


# Accessing Dictionary Items
# You can access the items of a dictionary by referring to its key name, inside square brackets [].

# Example:
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30

# Adding or Updating Items
# You can add a new key-value pair or update the value for an existing key using the assignment operator =.

my_dict["email"] = "john@example.com"  # Adds a new key-value pair
my_dict["age"] = 31  # Updates the value of an existing key
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

# Removing Items
# Several methods can remove items from a dictionary:

# pop(key): Removes the item with the specified key and returns the value.
# popitem(): Removes the last inserted key-value pair (before Python 3.7, removes an arbitrary pair) and returns it as a tuple.
# del dict[key]: Removes the item with the specified key.
# clear(): Removes all items from the dictionary.


my_dict.pop("email")
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

item = my_dict.popitem()
print(item)  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'age': 31}

del my_dict["age"]
print(my_dict)  # Output: {'name': 'John'}

my_dict.clear()
print(my_dict)  # Output: {}


# Dictionary Methods
# Dictionaries have several useful methods:

# keys(): Returns a view of the dictionary's keys.
# values(): Returns a view of the dictionary's values.
# items(): Returns a view of the dictionary's key-value pairs (as tuples).
# copy(): Returns a copy of the dictionary.
# update([other]): Updates the dictionary with the key-value pairs from other, overwriting existing keys.    
    
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(list(my_dict.keys()))  # Output: ['name', 'age', 'city']
print(list(my_dict.values()))  # Output: ['John', 30, 'New York']
print(list(my_dict.items()))  # Output: [('name', 'John'), ('age', 30), ('city', 'New York')]

new_info = {"age": 31, "email": "john@newexample.com"}
my_dict.update(new_info)
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@newexample.com'}

# Checking for Key Existence
# You can check if a key exists in a dictionary using the in and not in operators.

print("name" in my_dict)  # Output: True
print("email" not in my_dict)  # Output: False