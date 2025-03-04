while True:
	word = input("Enter a word: ").strip().lower()
		
	if word.isalpha():
		if word == word[::-1]:
			print(f"{word} is palindrome.")
		else:
			print(f"{word} is not palindrome.")
		break
	else:
		print("Invalid input. Please use only letters.")
