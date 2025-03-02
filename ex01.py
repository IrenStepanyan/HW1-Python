sum = 0

while True:

	print("Please enter your choice")
	print("1: for inputing the number")
	print("2: for displaying sum of all inputed numbers")
	choice = int(input("Your choice: "))
	if(choice == 1):
	
		num = int(input("Enter a number: "))
		sum += num
	
	elif(choice == 2):
	
		print(f"Sum of all inputed numbers: {sum}")
		break
	
	else:
		print("Invalide choice. Please try again")
