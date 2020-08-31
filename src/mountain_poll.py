responses = {}

polling_active = True

while polling_active:
	name = input("\b What is your name")
	response = input ("which mountain you want to climb today > ")

	# store the response in the dictionary
	responses[name] = response

	# repeat
	repeat = input("Would you let another person respond (yes/no) ? ")	
	if repeat == 'no':
		polling_active = False


# print results:
for name,response in responses.items():
	print(f"{name} would like to climb {response}")



