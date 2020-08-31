def build_person(first_name,last_name,age=None):
	""" Return dictornary of information of the person"""
	person = {'first_name':first_name,'last_name':last_name}
	if age:
		person['age'] = age
	return person

while True:
	print("\n Tell me your Name")
	print(" press q anytime to quit")
	f_name = input('First Name ::')
	if f_name == 'q':
		break

	l_name = input("Last Name ::")
	if l_name == 'q':
		break

	age = input("Age ::")	
	if age == 'q':
		break

	formatted_name = build_person(f_name,l_name,age)
	print(formatted_name)


