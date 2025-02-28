while True:
	try:
		ulist = input("Enter a list of numbers separated by space: ")
		if ulist.strip() == "":
			print("Empty list.")
		else:
			num_list = [int(x) for x in ulist.split()]
			total = sum(num_list)
			print(f"The sum of the numbers is: {total}.")
			break
	except:
		print("Invalid input. Try again.")
