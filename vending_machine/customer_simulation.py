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
	
	def __init__(self, lambda_param=3):
		'''
		Initializes a customer object specifying parameters for a 
		Poisson distribution. Defaults to lambda=3. This is interpreted
		as having an average of 3 customers arriving in a given unit
		of time. This is assumed to be 1 hour.
		'''
		self.lambda_param = lambda_param
		
	
	def pdf_func(self, k):
		
		'''
		Currently using a Poisson distribution assumption
		but can be extended to any discrete pdf
		'''
		return (self.lambda_param**k * math.exp(-self.lambda_param)) / (math.factorial(k))
		
	
	def calculate_arrivals(self, pdf_func=pdf_func):
		
		'''
		Calculates the number of arrivals in a given hour
		based on the assumed pdf. This is done by taking a RV~U(0, 1)
		and using a while loop to calculate the CDF.
		TODO: Update documentation
		'''
		
		self._rng = random.uniform(0, 1)
		self.arrival_counter = 0
		self._cdf_counter = self.pdf_func(self.arrival_counter)
		
		
		while self._cdf_counter < self._rng:
			self.arrival_counter += 1
			self._cdf_counter += self.pdf_func(self.arrival_counter)
			
		return self.arrival_counter
			

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
		try:
			return random.choice(drinks_display_list)
		except IndexError:
			 return None

		
		


if __name__ == "__main__":

	sample_customer = CustomerChoice()
	arrival_pattern = CustomerArrival()
	print(arrival_pattern.calculate_arrivals())
	print(arrival_pattern.arrival_counter)
	
