

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 
doubled_numbers = []
for number in numbers:
    doubled_number= number * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers)

# list comprehension
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)


str="hello"
print([char.upper() for char in str])


list1=[1,0,"hello","",[],[1,2,3]]
r=[bool(x) for x in list1]
print(r)

# list comprehension with if
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [number for number in numbers if number % 2 == 0]
print(evens)

# list comprehension with if else
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = ["even" if number % 2 == 0 else "odd" for number in numbers]
print(output)