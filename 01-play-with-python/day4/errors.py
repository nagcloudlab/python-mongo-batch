


# def colorize(text, color):
#     colors = ("cyan", "yellow", "blue", "green", "magenta")
#     if type(text) is not str:
#         raise TypeError("text must be instance of str")
#     if color not in colors:
#         raise ValueError("color is invalid color")
#     print(f"Printed {text} in {color}")


# try:
#     colorize("hello", "yellow")
# except (TypeError, ValueError) as e:
#     print(e)


# print("This is important code")

# ------------------------------------------------------------------------------------------------------------------------



# using pdb to debug



def add_and_multiply(a, b, c):
    result = a + b
    print(result)
    return result


print(add_and_multiply(1, 2, 3))
