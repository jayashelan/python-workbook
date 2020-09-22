def get_formatted_name(first,last,middle=''):
	"""Generate a neatly formatted full name"""
	if middle:
		 fullname = f"{first} {middle} {last}"
	else:
		fullname = f"{first} {last}"
		 
	return fullname.title()

			
