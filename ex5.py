from functools import lru_cache
@lru_cache(None) 
def factorial(n):
	if n ==0 or n ==1:
		return 1
	return n * factorial(n-1)

def main():
	while True:
		try:
			num = int(input("Enter a possitive number: "))
			if num < 0:
				print("Invalid input. Please enter a POSSITIVE number.")
			else: 
				print(f"The {num}! is {factorial(num)}.")
				break
		except: 
			print("Invalid input. Try again.")
main() 
