while True:
	try:
		num = input("Enter a number: ")
		dsum = 0
		for d in num:
			dsum +=int(d)
		print(f"The sum is {dsum}.")
		break
	except:
		print("Invalide input. Try again.")
