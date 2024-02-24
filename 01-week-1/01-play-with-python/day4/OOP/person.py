

# _name
# __name
# __name__


# class Person:
# 	# Init is a "dunder" method
#     def __init__(self):
#         self.name = "Tony"
#         # single underscore means "private" (sort of)
#         self._secret = "hi!"
#         # two leading underscores tells Python to "mangle" the name
#         self.__msg = "I like turtles!"
#         self.__lol = "HAHAHAHAH"


# p = Person()

# print(p.name)
# print(p._secret) #Anyone can still directly access the attribute

# print(dir(p)) # Notice what __msg and __lol have been "mangled" to

# print(p._Person__msg)
# print(p._Person__lol)


class Person:
    
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__salary = 0

    def say_full_name(self):
        print(f"{self.first_name} {self.last_name}")   

    def get_salary(self):
        return self.__salary     
    

p1 = Person("John","Doe",30)
p2 = Person("Jane","Doe",25)

print(p1.get_salary())