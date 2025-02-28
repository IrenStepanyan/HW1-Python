def Fibonacci(n):
	a = 0
	b = 1
	for i in range(n):
		print(a, end = " ")
		tmp = a
		a = b
		b = tmp + b

while True:
	try:
		num = int(input("Enter a number: "))
		Fibonacci(num)
		break
	except:
		print("Invalid input. Try again.")
