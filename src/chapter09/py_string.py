filename = 'pi1000000.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string=''

for line in lines:
	pi_string +=line.strip()

print(f"{pi_string[:52]}....")
print(len(pi_string))

birthday = input("Enter the birthday in the form of ddmm")

if birthday in pi_string:
	print("Your birthday is present in string")
else :
	print("Your birthday does not appear")

