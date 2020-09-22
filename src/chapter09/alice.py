
filename = "alice.txt"

try:
	with open(filename,encoding='utf-8') as file_object:
		content = file_object.read()

except FileNotFoundError:
		print(f"Sorry,the file {filename} does not exist")
else:
	# count approximately no of words
	words = content.split()
	num_words = len(words)

	print(f" the {filename} has {num_words} words in it")
