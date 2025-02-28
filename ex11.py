word = input("Enter a string: ")
count = 0

vowels="aeiouAEIOU"
for char in word:
	if char in vowels:
		count +=1
print(f"There are {count} vowels in {word}.")
