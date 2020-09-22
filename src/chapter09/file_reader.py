file_path ="D:\\work\\python\\python-workbook\\src\\chapter09\\text_files\\filename.txt"
with open (file_path) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
	