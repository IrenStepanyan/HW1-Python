while True:
	try:
		num = int(input("Enter a number: "))
		dsum = 0
		num = abs(num)
		for d in str(num):
			dsum +=int(d)
		print(f"The sum is {dsum}.")
		break
	except:
		print("Invalide input. Try again.")
