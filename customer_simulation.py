import random
import math


# All the customer needs is a drink name
# Assume uniform random dsn for now


class CustomerArrival:
	
	'''
	Assume a simple poisson process with a unit of time
	defined as an hour
	The class method should return an integer amount of arrivals
	Poisson parameter assumptions
	'''
	
	# We assume that average arrivals per hour is 3
	# Or, k = 3 and lambda = 1
	def __init__(self, k = 3, lambd = 1):
		self.prob_arrival = (lambd ** k) * math.exp(-lambd) / math.factorial(lambd)
		
	
	def calculate_arrivals(self):
		pass


class CustomerChoice:
	
	'''
  Object to contain information regarding customer choice
  given that customer has arrived at machine. This currently
  assumes a U(0, N) distribution for the probability of each drink
  being chosen.
	'''
	
	# Note: Would this depend on what's available in the machine?
	
	def __init__(self):
		
		'''
		Each instance would depend on what the customer sees on the front end.
		If there is no more coke, then coke would not be one of the choices.
		'''
		pass
	
	
	def choose_drink(self, drinks_display_list):
		'''
		This is currently random but can be extended in the future if required
		'''
		return random.choice(drinks_display_list)
		
		


if __name__ == "__main__":

	sample_customer = CustomerChoice()
	choice = sample_customer.choose_drink(["coke", "sprite", "fanta"])
	print(choice)
	
