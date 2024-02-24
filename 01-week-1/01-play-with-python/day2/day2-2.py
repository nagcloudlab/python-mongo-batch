


# how to create a function in python?

from datetime import datetime


def my_function():
    print("Hello from a function")

my_function() # call the function

# how to pass arguments to a function?

def my_function_with_args(username, greeting):
    print(f"Hello, {username} , From My Function!, I wish you {greeting}")

my_function_with_args("John Doe", "a great year!")

# how to return a value from a function?

def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(5, 7))


# ----------------------------------------------
# Function Arguments
# ----------------------------------------------


# Required arguments
# Keyword arguments
# Default arguments
# Variable-length arguments
# Keyword Dictionary arguments


# Required arguments
def required_argument(a, b):
    return a + b

print(required_argument(5,50))


# Keyword arguments
def keyword_argument(a, b):
    return a + b

print(keyword_argument(b=50, a=5))


# Example:
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus") 


# Default arguments
def default_argument(a, b=10):
    return a + b

print(default_argument(a=5, b=50))

# Variable-length arguments 
def variable_length_argument(*args):
    return sum(args)


print(variable_length_argument(1))
print(variable_length_argument(1, 2))
print(variable_length_argument(1, 2, 3))
print(variable_length_argument(1, 2, 3, 4))
print(variable_length_argument(1, 2, 3, 4, 5))


# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example:
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")

# Example:
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# ----------------------------------------------
# Pass statement
# ----------------------------------------------

# function definitions cannot be empty, 
# but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
    pass

# ----------------------------------------------
# Principles of Function
# ----------------------------------------------

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# in python, function is a first class citizen, 

#    - A function can be stored in a variable
#    - A parameter of a function can be a function
#    - The return value of a function can be a function

# ----------------------------------------------

# - A function can be stored in a variable

def greet():
    print("Hello")

say_hello = greet
say_hello()

# - A parameter of a function can be a function

def greet(tbg=None):
    print("😊😊😊😊😊😊😊😊")
    if tbg:
        tbg()
    else:    
        print("greetings")
    print("😊😊😊😊😊😊😊😊")

greet()


def timeBasedGreeting():
    current_local_hour=datetime.now().hour
    if current_local_hour < 12:
        print("Good Morning")
    elif current_local_hour < 18:
        print("Good Afternoon")
    else:
        print("Good Evening")

greet(timeBasedGreeting)        
    

# - The return value of a function can be a function

def teach():
    print("I am teaching Python")
    def learn():
        print("I am learning Python")
    print("teaching ends")
    return learn

learnFn = teach()
learnFn()
learnFn()

# ----------------------------------------------
#  Higher Order Function ( HOF )
# ----------------------------------------------

#  Design issues

# -> code tangling aka spaghetti code (tight coupling)
# -> code scattering ( duplicate code)

# Solution:

    # -> using higher order function ( HOF )

# ----------------------------------------------

def hello():
    print("Hello")

def hi():
    print("Hi")

# hello()
# hi()
    
def withSmile(f):
    def wrapper():
        print("😊😊😊😊😊😊😊😊")
        f()
        print("😊😊😊😊😊😊😊😊")
    return wrapper

hello()
withSmile(hello)()

hi()
withSmile(hi)()

# ----------------------------------------------


    
    









