def get_formatted_name(first_name,last_name,middile_name=''):
	"""Return a full name, neatly formatted"""
	if middile_name:
		full_name = f"{first_name} {last_name}"
	else:
		full_name = f"{first_name} {middile_name} {last_name}"		
	
	full_name =f"{first_name} {middile_name} {last_name}"
	
	return full_name.title()

musician = get_formatted_name('Jay','Boobalan' )	
print(musician)
musician = get_formatted_name('Jay','Boobalan','krishnan' )	
print(musician)
