def count_words(filename):
	"""Count the approximate no of words in the file:::"""
	try:
		with open(filename,encoding='utf-8') as f:
			content = f.read()

	except FileNotFoundError:
		#print(f"Sorry !! File name {filename} no found")
		pass

	else:
		 words = content.split()
		 num_words = len(words)
		 print(f'The file {filename} has {num_words} of words in it')		


filenames = ['alice.txt','sidartha.txt','mocky_dick.txt','little_woman.txt']
for filename in filenames:
	count_words(filename)

