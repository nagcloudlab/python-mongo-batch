from datetime import datetime
from functools import reduce

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


total_price=reduce(lambda acc,next: acc+next, map(lambda menuItem: menuItem["price"],menu),0)
print(total_price)

