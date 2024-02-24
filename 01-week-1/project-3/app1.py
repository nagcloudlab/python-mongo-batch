

# print(1+1)
# print("1"+"1")
# print([1]+[1])

from copy import copy

class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		
	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age

	def __add__(self, other):
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!"

	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "CANT MULTIPLY!"
	


human1 = Human("Jenny", "Larsen", 47)

print(human1)
print(len(human1))

human2 = Human("Buddy", "Larsen", 47)

human3 = human1 + human2
print(human3)

triplets = human1 * 3
print(triplets)	
