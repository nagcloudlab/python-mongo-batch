from random import randint

# data types

# 1. int
# 2. float
# 3. bool
# 4. str

# 5. list
# 6. tuple
# 7. set
# 8. dict


# 1. int
# int is a whole number, positive or negative, without decimals, of unlimited length.
# int data type is used to represent integer numbers.
# int data type is a 4 byte number and ranges from -2147483648 to 2147483647.

# Example
x = 1
y = 35656222554887711
z = -3255522
print(x)
print(type(x))

# 2. float
# float is a number, positive or negative, containing one or more decimals.
# float data type is used to represent decimal numbers.
# float data type is a 8 byte number and ranges from -1.7E+308 to 1.7E+308.

# Example
x = 1.10
y = 1.0
z = -35.59
print(x)
print(type(x))

# 3. bool
# bool is a data type that can only take the values True or False.
# bool data type is used to represent boolean values.

# Example
x = True
y = False
print(x)
print(type(x))


# 4. str
# str is a data type that can store a sequence of characters.
# str data type is used to represent string values.

# Example
x = "Hello World"
y = 'Hello World'
print(x)
print(type(x))

# format string
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

#  > python 3.6
name = "John"
age = 36
txt = f"My name is {name}, and I am {age}"


# Type Conversion
# You can convert from one type to another with the int(), float() methods:

x = 1    # int
y = 2.8  # float

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

print(a)
print(type(a))


# arithmatic operators

# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

# Example
x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


# relational operators

# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

# Example
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# logical operators

# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Example
x = 5

print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

