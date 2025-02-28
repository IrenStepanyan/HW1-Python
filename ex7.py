while True:
	try:
		num = int(input("Enter a number: "))
		for x in range(1, 11):
			print(f"{num}*{x} = {num*x}")
		break
	except:
		print("Invalid input. Try again.")
