def make_pizza(size,*toppings):
	""" Print the list of toppings that have been requested """
	print(f"Make a {size} -inch pizza with the following topppings")
	for topping in toppings:
		print(f" - {topping}")