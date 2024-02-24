
# python function

def my_function():
    print("Hello from a function")

my_function()  # Output: Hello from a function

# Arguments
# Information can be passed to functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")  # Output: Emil Refsnes

my_function("Tobias")  # Output: Tobias Refsnes

my_function("Linus")  # Output: Linus Refsnes

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# Number of Arguments

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# Example:
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")  # Output: Emil Refsnes

# my_function("Emil")  # Output: TypeError: my_function() missing 1 required positional argument: 'lname'

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example:
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  # Output: The youngest child is Linus

# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# Example:
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")  # Output: The youngest child is Linus

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example:
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")  # Output: His last name is Refsnes

# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:

# Example:
def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")  # Output: I am from Sweden

my_function("India")  # Output: I am from India

my_function()  # Output: I am from Norway

my_function("Brazil")  # Output: I am from Brazil

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# Example:
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)  # Output: apple banana cherry

# Return Values

# To let a function return a value, use the return statement:

# Example:
def my_function(x):
    return 5 * x

print(my_function(3))  # Output: 15

print(my_function(5))  # Output: 25

print(my_function(9))  # Output: 45

# The pass Statement

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example:
def myfunction():
    pass

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)  # Output: 21


# how to create a function in python

# To create a function in Python, you will start with the def keyword, followed by the name of the function, parentheses, and a colon. The function name should be descriptive of what the function does. The parentheses may include arguments, which are the values that are passed into the function. The body of the function is indented, and contains the code that will be executed when the function is called.

# Example:
def my_function():
    print("Hello from a function")

# Calling a function
# To call a function, use the function name followed by the parentheses.
    
# Example:
my_function()  # Output: Hello from a function

# Lambda Function
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Example:
# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a: a + 10

print(x(5))  # Output: 15

# Lambda functions can take any number of arguments:

# Example:
# A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b: a * b

print(x(5, 6))  # Output: 30

# Example:
# A lambda function that sums argument a, b, and c and print the result:

x = lambda a, b, c: a + b + c

print(x(5, 6, 2))  # Output: 13

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# Example:
def myfunc(n):
    return lambda a: a * n

# Use that function definition to make a function that always doubles the number you send in:

# Example:
mydoubler = myfunc(2)

print(mydoubler(11))  # Output: 22

# Or, use the same function definition to make a function that always triples the number you send in:

# Example:
mytripler = myfunc(3)

print(mytripler(11))  # Output: 33
# Use lambda functions when an anonymous function is required for a short period of time.
# Python also accepts function recursion, which means a defined function can call itself.


# functional programming in python

# assign the lambda function to a variable and use the variable to call the function.

# Example:
x = lambda a: a + 10

print(x(5))  # Output: 15
