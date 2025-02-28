def second_largest(numbers):
	nums = list(set(numbers))
	nums.sort(reverse = True)
	if len(nums) > 1:
		return nums[1]
	else:
		return None

try:
	ulist = input("Enter a list of numbers separated by a space: ")
	num_list = [int(x) for x in ulist.split()]
	result = second_largest(num_list)
	
	if result is not None:
		print(f"The secong largest number is: {result}.")
	else:
		print("There is no second largest number.")
except:
	print("Invalid error. Please try again.")
