

# We can pass funcs as args to other funcs

# def sum(n, func):
# 	total = 0
# 	for num in range(1,n+1):
# 		total += func(num)
# 	return total


# def square(x):
# 	return x*x

# def cube(x):
# 	return x*x*x


# print(sum(3,cube))
# print(sum(3,square))



# from random import choice
# # We can return funcs from other funcs
# def make_laugh_func():
#     def get_laugh():
#         l = choice(('HAHAHAH', 'lol', 'tehehe'))
#         return l

#     return get_laugh

# laugh = make_laugh_func()
# print(laugh())



# // HOF ==> decorators 

# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# def greet():
#     print("My name is Colt.")

# def rage():
# 	print("I HATE YOU!")

# # we are decorating our function 
# # with politeness!
# greet = be_polite(greet)

# polite_rage = be_polite(rage)
# polite_rage()


# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper


# @be_polite
# def greet():
#     print("My name is Colt.")


# @be_polite
# def rage():
# 	print("I HATE YOU!")


# greet()
# rage()



# Let's define a speed_test decorator
from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper



@speed_test
def sum_nums_gen():
	return sum(x for x in range(90000000))


@speed_test
def sum_nums_list():
	return sum([x for x in range(90000000)])




print(sum_nums_gen())
print(sum_nums_list())












