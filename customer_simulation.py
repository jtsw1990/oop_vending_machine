import random
import math


# All the customer needs is a drink name
# Assume uniform random dsn for now


class CustomerArrival:
	
	'''
	Assume a simple poisson process with a unit of time
	defined as an hour
	The class returns a probability of arrival in a given unit of time
	'''
	
	# We assume that average arrivals per hour is 3
	# Or, k = 3 and lambda = 1
	def __init__(self, k = 3, lambd = 1):
		self.prob_arrival = (lambd ** k) * math.exp(-lambd) / math.factorial(lambd)


class CustomerChoice:
	
	'''
  Object to contain information regarding customer choice
  given that customer has arrived at machine. This currently
  assumes a U(0, N) distribution for the probability of each drink
  being chosen.
	'''
	
	# Note: Would this depend on what's available in the machine?
	
	def __init__(self, drinks_display_count):
		
		'''
		Each instance would depend on what the customer sees on the front end.
		If there is no more coke, then coke would not be one of the choices.
		'''
	
		self.customer_rng = random.randint(0, drinks_display_count - 1)
		
		


if __name__ == "__main__":

	test = CustomerChoice(5)
	print(test.customer_rng)
	test_2 = CustomerArrival()
	print(test_2.prob_arrival)
	
	
