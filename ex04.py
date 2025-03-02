import random

num = random.randint(1,11)
attempts = 0

while True:
	try:
		guess = int(input("Guess a number between 1 and 10: "))
		if guess > num:
			print("Too high. Try again.")
			attempts +=1
		elif guess < num: 
			print("Too low. Try again.")
			attempts +=1
		else:
			print(f"You won!!!\nThe number was: {num}")
			break
	except:
		print("Invalid input. Please try again.")
