class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗蹲下"""
		print(self.name.title() + " is now sitting!")

	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " rolled over!")

dog1 = Dog('dubo', 18)
print(dog1.name)
print(dog1.age)
dog1.sit();
dog1.roll_over();


class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' +self.model
		return long_name.title()

	def read_odometer(self):
		print('This car has ' + str(self.odometer_reading) + ' miles on it.')

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cant roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles


class ElectricCar(Car):
	"""电动汽车的独特之处"""

	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery_size = 700

	def describe_battery(self):
		print('This car has a ' + str(self.battery_size) + '-kWh battery')


tesla = ElectricCar('tesla', 'model s', 2016)
print(tesla.get_descriptive_name())
tesla.describe_battery()