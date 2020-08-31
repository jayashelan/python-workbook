def describe_pet(pet_name,animal_type='dog'):
	"""Display information abt the pet"""
	print(f"\n I have a {animal_type}")
	print(f" My {animal_type} name is {pet_name} ")



describe_pet('hamster','harry')	
describe_pet('dog','willie')

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')

describe_pet(pet_name='willie')

describe_pet('willie')

describe_pet('willie','hamster')


describe_pet()
