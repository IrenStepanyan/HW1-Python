while True:
	try:
		n1 = int(input("Enter the number1: "))
		n2 = int(input("Enter the number2: "))
		n3 = int(input("Enter the number3: "))
		max_num = n1
		if(max_num < n2):
			max_num = n2
		if max_num < n3:
			max_num = n3
		print(f"The maximum number is: {max_num}")
		break
	except:
		print("Invalid input. Please try again.")
