class Dog:
	""" A simple attempt to model a Dog """

	def __init__(self,name,age):
		"""initialise the name and age"""
		self.name = name
		self.age = age

	def sit(self):
		"""simulate a dog sitting in response to a command """
		print(f"{self.name} is now sitting")

	def roll_over(self):
		"""Simulate rolling over in response to a command """
		print(f"{self.name} roller over")


my_dog = Dog('willie',6)

print(f"My dog name is {my_dog.name}.")
print(f"My dog age is {my_dog.age}")

my_dog.sit()

my_dog.roll_over()


your_dog = Dog('harry',12)

print(f"Your dog name is {your_dog.name}")
print(f"Your dog age is {your_dog.age}")

your_dog.sit()
your_dog.roll_over()





		