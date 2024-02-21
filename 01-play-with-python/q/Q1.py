

numbers=[1,2,3,4,5,6,7,8,9,10]

def sum_of_numbers(numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum

print(sum_of_numbers(numbers))

# find average of numbers

def average_of_numbers(numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum/len(numbers)

print(average_of_numbers(numbers))

# find maximum of numbers

def maximum_of_numbers(numbers):
    max=numbers[0]
    for number in numbers:
        if number>max:
            max=number
    return max

print(maximum_of_numbers(numbers))
