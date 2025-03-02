while True:
	try:
		num = int(input("Enter a number (0 for exit): "))
		if( num == 0): 
			break;
		elif(num % 2 == 0) :
			print(f"{num} is even.")
		elif(num % 2 != 0) :
			print(f"{num} is odd.")
	except ValueError:
		print(f"Invalid input. Please try again.")
