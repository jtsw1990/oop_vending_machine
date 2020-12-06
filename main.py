from vending_machine import DrinksData, VendingMachine
from customer_simulation import CustomerArrival, CustomerChoice


PERIOD_IN_HOURS = 24

vending_one = VendingMachine("drinks_list.csv")
sample_customer = CustomerArrival()
sample_customer_choice = CustomerChoice()

# customer_options = CustomerChoice(len(vending_one.drinks_displayed))


for hour in range(PERIOD_IN_HOURS):
	arrived_per_unit_time = sample_customer.calculate_arrivals()
	print("{} customers arrived in time {}".format(arrived_per_unit_time, hour + 1))
	for customer in range(arrived_per_unit_time):
		drinks_displayed = vending_one.drinks_displayed
		drink_choice = sample_customer_choice.choose_drink(drinks_displayed)
		vending_one.dispense_drink(drink_choice)
		print("Customer: {} from time: {} chose: {}".format(customer + 1, hour + 1, drink_choice))
		print("Drinks left: {}, Cumulative Earnings: {}".format(vending_one._current_stock, vending_one._current_earnings))
	# Finally tabulate totals
	# Fit into analytics pipeline	
	pass
	
	
	
	




