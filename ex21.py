def amstrong_num(num):
	num_str = str(num)
	num_len = len(num_str)
	total = sum(int(d) ** num_len for d in num_str)
	if(total == num):
		return True
	else:
		return False
try:
	num = int(input("Enter a number: "))
	if amstrong_num(num):
		print(f"{num} is an Armstrong number.")
	else:
		print(f"{num} is not an Armstrong number.")
except:
	print("Invalid input. Please try again.")
