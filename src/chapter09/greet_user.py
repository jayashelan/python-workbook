import json


def get_stored_username():
	"""Get Stored User name if available"""
	filename ='username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except Exception as e:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for new User"""
	username = input("What is your Name ::")
	filename = 'username.json'
	with open(filename,'w') as f:
		json.dump(username,f)
	return username	



def greet_user():
	"""Greet User by name"""
	username = get_stored_username()

	if username:
		print(f"Welcoome back {username}")
	else:
		username = get_new_username()
		
		
greet_user()

