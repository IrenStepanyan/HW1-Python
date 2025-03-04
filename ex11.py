while True:
	word = input("Enter a string: ")
	count = 0
	vowels="aeiouAEIOU"
	if word.isalpha():
		for char in word:
			if char in vowels:
				count +=1
		print(f"There are {count} vowels in {word}.")
		break
	else:
		print("Invalid input. Please try again without using number.")
