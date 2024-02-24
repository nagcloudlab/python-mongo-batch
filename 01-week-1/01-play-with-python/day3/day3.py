from datetime import datetime
from functools import reduce

# from builtins import *

#
# def my_function(x,y,*args,z=10,**kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(z)
#     print(kwargs)

# my_function(1,2)
# my_function(x=1,y=2)
# my_function(y=2,x=1)
# my_function(1,y=2)

# my_function(1,2,*[3,4,5],*(6,7,8),z=20,**{"name":"ponmurugan","age":30})


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10]
#
# def my_double_function(x):
#     return x * x

# my_double_function = lambda x: x * x

# my_doubled = tuple(map(lambda x:x*x, my_list))
# print(my_doubled)


menu = [
    {"name": "idly", "price": 30},
    {"name": "dosa", "price": 40},
    {"name": "pongal", "price": 50},
    {"name": "vada", "price": 20},
    {"name": "poori", "price": 30},
    {"name": "chapathi", "price": 40},
    {"name": "parotta", "price": 50},
    {"name": "briyani", "price": 100},
    {"name": "meals", "price": 60},
    {"name": "fried rice", "price": 70},
]


#
# lowCostMenu = list(map(lambda menuItem: menuItem["name"],
#                        filter(lambda menuItem: menuItem["price"] < 50, menu))
#                    )
#
# for item in lowCostMenu:
#     print(item)
#
#
# total_price=reduce(lambda acc,next: acc+next, map(lambda menuItem: menuItem["price"],menu),0)
# print(total_price)

# --------------------------------------------------------------
# // Closures
# --------------------------------------------------------------


# def teach(sub):
#     print(f"teaching {sub}")
#     notes = f"notes of {sub}"
#
#     def learn():
#         print(f"learning with {notes}")
#
#     print(f"teaching {sub} ends")
#     return learn
#
#
# learnFn = teach("python")
#
# learnFn()
#

# What is a Closure?
# A closure is a function object that remembers values in enclosing scopes
# even if they are not present in memory.
# It's a record that stores a function together with an environment:
# a mapping associating each free variable of the function (variables that are used locally but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.


# Closures are used for:

# Encapsulating data (to hide it from the outside world)
# Implementing callbacks, decorators, and factories
# Maintaining state in an object-oriented way without using classes


# How Closures Work
# A closure occurs when a nested function references a value in its enclosing scope.
# The criteria for creating a closure are:

# We must have a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.

# --------------------------------------------------------------
# Encapsulating data (to hide it from the outside world)
# --------------------------------------------------------------

# e.g counter module

def counter():
    count = 0  # private variable ( data hiding )

    def f():  # private function
        pass

    def inc():
        nonlocal count
        count += 1

    def get():
        return count

    return inc, get


# inc, get = counter()
# inc()
# inc()
# inc()
# print(get())
#
# i, g = counter()
# i()
# i()
# print(g())

# def wrapper(htmlEle, msg):
#     return f"<{htmlEle}>{msg}</{htmlEle}>"
#
# print( wrapper("h1", "Hello") )
# print( wrapper("h1", "Hi") )
# print( wrapper("h1", "Hola") )


# def wrapper(htmlEle):
#     def wrapText(msg):
#         return f"<{htmlEle}>{msg}</{htmlEle}>"
#     return wrapText
#
# h1 = wrapper("h1")
#
# print(h1("Hello"))
# print(h1("Hi"))
#
# p = wrapper("p")
#
# print(p("Hello"))
# print(p("Hi"))


# built-in functions

# sum([1, 2, 3, 4, 5])

# --------------------------------------------------------------


menu = [
    {"name": "idly", "price": 30},
    {"name": "dosa", "price": 40},
    {"name": "pongal", "price": 50},
    {"name": "vada", "price": 20},
    {"name": "poori", "price": 30},
    {"name": "chapathi", "price": 40},
    {"name": "parotta", "price": 50},
    {"name": "briyani", "price": 100},
    {"name": "meals", "price": 60},
    {"name": "Piza", "price": 70},
]

# --------------------------------------------------------------

# isAllTrue=all(map(lambda menuItem: menuItem["name"],menu));
# print(isAllTrue)
#

# --------------------------------------------------------------

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
sortedNumbers=sorted(numbers)
print(sortedNumbers)
