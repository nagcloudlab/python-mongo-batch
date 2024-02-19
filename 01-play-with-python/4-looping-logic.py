
# times = input("How many times do I have to tell you? ")
# times = int(times)

# Simplest Version
# for time in range(times):
# 	print("CLEAN UP YOUR ROOM")

# Version 2
# for time in range(times):
# 	print(f"time {time+1}:CLEAN UP YOUR ROOM")
	

for num in range(1,21):
	if num == 4 or num == 13:
		print(f"{num} is unlucky")
	elif num % 2 == 0:
		print(f"{num} is even")
	else:
		print(f"{num} is odd")


#--------------------------------

# Continues to ask for user input until the user types 'bananas'
msg = input("whats the secret password?")
while msg != "bananas":
	print("WRONG!")
	msg = input("whats the secret password?")
print("CORRECT!")


for num in range(1,11):
	print(num)

# equivalent of above for loop
# num = 1
# while num < 11:
# 	print(num)
# 	num += 1
	
#--------------------------------

# print("-"*10)

# With a for loop
# for x in range(3):
# 	for num in range(1,11): 
# 		print("\U0001f600" * num)


# With a while loop
times = 1
while times < 11:
	print("\U0001f600" * times)
	times += 1

#--------------------------------

# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == "exit"):
#         break

# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break

times = int(input("How many times do I have to tell you? "))

for time in range(times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 3: 
		print("do you even listen anymore?")
		break
		

#--------------------------------
