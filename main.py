from vending_machine import DrinksData, VendingMachine
from customer_simulation import CustomerArrival, CustomerChoice


PERIOD_IN_HOURS = 24

vending_one = VendingMachine("drinks_list.csv")
customer_options = CustomerChoice(len(vending_one.drinks_displayed))


for hour in range(PERIOD_IN_HOURS):
	# Find out how many customers actually arrived
	# Find out the choice of drinks for each customer
	# Run methods dispense drink
	
	# Finally tabulate totals
	# Fit into analytics pipeline	




