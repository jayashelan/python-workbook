print("Give me 2 numbers i will divide them")
print("Enter 'q' to quit")

while True:
	first_number = input("\First Number:: ")
	if first_number == 'q':
		break

	second_number = input("\n Second Number ::")

	if second_number =='q':
		break
	try:
		answer = int(first_number)/int(second_number) 
	except Exception as e:
		print(f"You can't divide by {first_number} {second_number}")
	else:
		print(answer)	
	
		
	




