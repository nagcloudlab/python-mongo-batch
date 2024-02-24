
# way-1

# class FileContextManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         print('Entering the context')
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         print('Exiting the context')
#         self.file.close()


# with FileContextManager('test.txt', 'w') as file:
#     file.write('Hello, World!')        


# way-2

# from contextlib import contextmanager

# @contextmanager
# def file_manager(filename, mode):
#     try:
#         file = open(filename, mode)
#         yield file
#     finally:
#         file.close()

# with file_manager('test.txt', 'w') as file:
#     file.write('Hello, World!')


# way-3


# # write a file
# with open('test.txt', 'w') as file:
#     file.write('Hello, World!')

# # read a file
# with open('test.txt', 'r') as file:
#     print(file.read())
