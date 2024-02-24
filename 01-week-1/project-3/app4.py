
# def square_numbers_v1(numbers):
#     result=[]
#     for number in numbers:
#         result.append(number*number)
#     return result

# my_nums=square_numbers_v1([1,2,3,4,5])




# it=square_numbers_v2([1,2,3,4,5])
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # StopIteration



# # ------------------------------------------------------------------

# import psutil
# import random
# import datetime

# names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
# majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print('Memory (Before): {}Mb'.format(psutil.virtual_memory().percent))


# names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
# majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


# def people_list(num_people):
#     result = []
#     for i in range(num_people):
#         person = {
#                     'id': i,
#                     'name': random.choice(names),
#                     'major': random.choice(majors)
#                 }
#         result.append(person)
#     return result


# def people_generator(num_people):
#     for i in range(num_people):
#         person = {
#                     'id': i,
#                     'name': random.choice(names),
#                     'major': random.choice(majors)
#                 }
#         yield person



# # t1 = datetime.datetime.now()
# # people = people_list(10000000)
# # t2 = datetime.datetime.now()


# t1 = datetime.datetime.now()
# people = people_generator(10000000)
# t2 = datetime.datetime.now()

# for p in people:
#     print(p)


    
# print('Memory (After): {}Mb'.format(psutil.virtual_memory().percent))
# print('Took {} Seconds'.format(t2-t1)    )


# # ------------------------------------------------------------------

list1 = [1,2,3,4,4,5]
# list2 = [n*n for n in list1] # list comprehension
# print(list2)


# def square_numbers_v2(numbers):
#     for number in numbers:
#         yield number*number
gen=(n*n for n in list1) # generator
print(list(gen))
# print(set(gen))

# ------------------------------------------------------------------


