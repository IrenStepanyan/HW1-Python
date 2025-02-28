def gcd(a,b):
	while b:
		a, b = b,  a%b
	return a

try:
	n1 = int(input("Enter the fist number: "))
	n2 = int(input("Enter the second number: "))
	print(f"The grestest common divisor of {n1} and {n2} is {gcd(n1, n2)}")
except:
	print("Invalid input. Please try again.")
