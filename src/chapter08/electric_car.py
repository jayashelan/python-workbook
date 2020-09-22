class Car:
	"""A simple atempt to represent a car"""

	def __init__(self,model,make,year):
		self.model = model
		self.make = make
		self.year = year
		self.odometer_reading = 0
		self.battery_size = 75

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} on it")

	def update_odometer(self,milage):
		if(milage > self.odometer_reading):
			self.odometer_reading += milage
		else:
			print("You can't rollback an odometer")

	def increment_odometer(self,miles):
		self.odometer_reading += miles

	def describe_battery(self):
		"""Print the statement describing the battery size"""
		print(f"The car has a {self.battery_size} -KWh battery")

	def fill_gas_tanl(self):
		"""Print the gas tank status"""
		print("Filling the gas tank !!!")
		print("Gas tank is full !!!")


class Battery:
	"""A simple attempt to model battery for Electric Car"""

	def __init__(self,battery_size = 75):
		"""initialize the battery's attribute"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print(f"This Car has a {self.battery_size} -KWh battery.")
	
	def get_range(self):
		"""Print a statement abt the range this battery provides"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		
		print(f"This car can go abt {range} miles in full charge")






class ElectricCar(Car):
	"""Represent the aspect of a Car, specific to ElectricCar"""
	def __init__(self,model,make,year):
		""" initialize attributes of the parent class """
		super().__init__(make,model,year)
		self.battery = Battery()

	def fill_gas_tanl(self):
		"""Electric Car doesn't have a gas tank"""
		print("This car does not have a gas tank")


my_tesla = ElectricCar('tesla','model s',2019 )		
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tanl()
my_tesla.battery.get_range()

			


