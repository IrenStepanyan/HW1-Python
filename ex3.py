while True:
	print("Menu")
	print("1: Addition")
	print("2: Substraction")
	print("3: Multiplication")
	print("4: Division")
	print("5: Exit")
	choice = input("Your choice: ")
	
	if(choice =="5"):
		break
	elif(choice =="1" or choice =="2" or choice =="3" or choice =="4"):
		try:
			num1 = int(input("Enter Number1: "))
			num2 = int(input("Enter Number2: "))
			if choice == "1":
				print(f"{num1} + {num2} = {num1+num2}")
			elif choice == "2":
				print(f"{num1} - {num2} = {num1 - num2}")
			elif choice == "3":
				print(f"{num1} * {num2} = {num1*num2}")
			elif choice == "4":
				if(num2 != 0):
					print(f"{num1}/{num2} = {num1/num2}")
				else:
					print("Error: Cannot divide by zero.")
		except: 
			print("Invalid input.")
	else:
		print("Invalide input. Please try again.")		
