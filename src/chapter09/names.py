
from name_function import get_formatted_name

print(f"Enter q at any time to quit")
while True:
	first = input("\n Please give the first name:")
	if first =='q':
		break
	last = input("\n Please give the last name:")
	if last =='q':
		break
	formatted_name = get_formatted_name(first,last)
	print(f"\nNeatly formatted name:{formatted_name}")



