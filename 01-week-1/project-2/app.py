
# class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


# object
my_dog = Dog("Rex", 5)
print(my_dog.bark())  # Rex says woof!


# Encapsulation

class Car:
    def __init__(self, speed=0):
        self.__speed = speed  # Private attribute

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

car = Car(100)
# print(car.__speed)  # AttributeError: 'Car' object has no attribute '__speed'
print(car.get_speed())  # 100
car.set_speed(150)
print(car.get_speed())  # 150

# print(dir(car))  # ['_Car__speed', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_speed', 'set_speed']


# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # print("Some animal sound")
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")



# Polymorphism
        

# duck typing
# definition: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."


def animal_sound(animal):
    animal.speak()



cat = Cat("Kitty")
dog = Dog("Rex")

# cat.speak()  # Some animal sound
# dog.speak()  # Some animal sound

animal_sound(cat)  # Kitty says Meow!
animal_sound(dog)  # Rex says Woof!    
animal_sound("Hello")  # AttributeError: 'str' object is not callable


# Abstraction

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height