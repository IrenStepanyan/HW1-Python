while True:
	word = input("Enter a string: ").strip()

	if word =="":
		print("Invalide input! Try again.")
	else:
		break 

revstr = word[::-1]
print("The reverse string is: ", revstr)
