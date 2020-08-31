def print_modles (unprinted_designs,completed_models):
	"""
	Simulate printing each design,until none are left
	Move each design to completed models after printing
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing the design {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	""" Show all the models that are printed """
	print("\n The following models has been printed ")
	for completed_model in completed_models:
		print(completed_model)

# start with some design that need to be printed
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_modles(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
