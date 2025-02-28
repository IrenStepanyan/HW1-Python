ulist = input("Enter a list of items separated by space: ")

if ulist.strip() == "":
	items = []
else:
	items = ulist.split(' ')
print(f"The length of the list is: {len(items)}")
