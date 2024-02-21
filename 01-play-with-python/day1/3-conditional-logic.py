from random import randint


x=1
print(x==1) # True
print(x is 1) # True
print(x is not 1) # False

# important note , falsy values in python
# False, None, 0, "", (), [], {}
# all other values are truthy values

# Example-1
x = 1
y = 10
if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")


# Example-2

v=None
if v:
    print("v is truthy")


# Example-3
x = ""
if x:
    print("x is truthy")
else:
    print("x is falsy")


# Example-4
x = 0
if x:
    print("x is truthy")
    if x is 0 and x is not None:
        print("x is 0")
else:
    print("x is falsy")


# Example-5
x=10
if x:
    print("x is truthy")
else:
    print("x is falsy")


# --------------------------------------------
    
color = input("What's your favorite color?")
if color == 'purple':
	print("excellent choice!")
elif color == 'teal':
    print("not bad!")
elif color == 'seafoam':
    print("mediocre")
elif color == 'pure darkness':
    print("I like how you think")
else: 
	print("YOU MONSTER!") 


# --------------------------------------------
     
animal = input("enter your favorite animal")

if animal:
    print(animal + " is my favorite too!")
else:
	print("YOU DIDNT SAY ANYTHING!")     
     
# --------------------------------------------
      
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You are good to go and can drink")
    elif age >= 18:
        print("You can enter, but need a wristband!")
    else:
        print("You can't come in, little one! :(")
else:
    print("Please enter an age!")        

# --------------------------------------------
	

print("Rock...")
print("Paper...")
print("Scissors...")
player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")


