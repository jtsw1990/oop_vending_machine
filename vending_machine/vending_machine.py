import csv


class DataReader:
	'''
	Object to read in initial drinks data set
	to be used as input in VendingMachine class
	'''

	def __init__(self, filepath):
		self.df = []
		with open(filepath, "r") as file:
			my_reader = csv.reader(file, delimiter=",")
			next(my_reader)
			for row in my_reader:
				self.df.append(row)


class VendingMachine:
	'''
	Insert doc string here
	'''
				
	def __init__(self, max_capacity):
		print("__init__ is being called here")
		self.max_capacity = max_capacity
		self.current_earnings = 0
		self.current_stock = 0
		self.stock_list = None
		self.drinks_displayed = None
			
	def __repr__(self):
		print("__repr__ was being called here")
		return "VendingMachine({!r})".format(self.max_capacity)
	
	@property
	def max_capacity(self):
		print("max_cap property being called here")
		return self.__max_capacity

	@max_capacity.setter			
	def max_capacity(self, max_capacity):
		print("max_cap setter called here")
		if not isinstance(max_capacity, (int, float)):
			raise TypeError("Please enter an integer value") 
		elif max_capacity < 0:
			raise ValueError("Capacity cannot be negative")
		elif max_capacity % 1 != 0:
			raise TypeError("Please enter an integer value")
		else:
			self.__max_capacity = max_capacity
							
	def load_drinks(self, filepath):
		self.drink_list = DataReader(filepath).df
		if self.stock_list is None:
			self.stock_list = {
			row[0]: [float(row[1]), int(row[2])]
			for row in self.drink_list
		}
		current_stock = sum([
			value[-1] for key, value in self.stock_list.items()
		])
		if current_stock > self.max_capacity:
			raise ValueError("Loaded drinks past capacity")
		else:
			self.current_stock = current_stock
	
	def display_stock(self):
		self.drinks_displayed = [
			x[0] for x in list(self.stock_list.items()) if x[-1][-1] > 0
			]
		return self.drinks_displayed

	def dispense_drink(self, drink_name):
		
		'''
		Method to simulate a vending machine object
		dispensing a drink. Returns drink_name as a string if available.
		Returns None if out of stock.
		'''
		try:
			if self.stock_list[drink_name][-1] > 0:
				self.stock_list[drink_name][-1] -= 1
				self.current_earnings += self.stock_list[drink_name][0]
				self.current_stock = sum([value[-1]
					for key, value in self.stock_list.items()])
				return drink_name
			else:
				return None
		except KeyError:
			print("Machine out of stock")
			return None
		


if __name__ == "__main__":
	test = VendingMachine(200)
	test.load_drinks("drinks_list.csv")
	test.display_stock()
	for i in range(150):
		test.dispense_drink("coke")
		test.dispense_drink("ice_lemon_tea")
		test.dispense_drink("fanta_orange")
		test.dispense_drink("fanta_grape")
		test.dispense_drink("sprite")
		test.dispense_drink("pepsi")
		test.dispense_drink("mountain_dew")
	print(test.stock_list)
	print(test.display_stock())

