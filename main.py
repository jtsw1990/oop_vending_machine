from vending_machine.vending_machine import DataReader, VendingMachine
from vending_machine.customer_simulation import CustomerArrival, CustomerChoice
import time
import datetime
import csv
from datetime import datetime
import os
import json


with open("config.json") as f:
    config = json.load(f)


PERIOD_IN_HOURS = config["HOURS"]
ts = datetime.now().strftime("%d-%m-%y_%H-%M")
output_folder = "./analytics/{}".format(ts)

vending_one = VendingMachine(config["MAX_CAPACITY"])
vending_one.load_drinks("./vending_machine/drinks_list.csv")
sample_customer = CustomerArrival()
sample_customer_choice = CustomerChoice()


if not os.path.exists(output_folder):
	try:
		os.makedirs(output_folder)
	except OSError as exc:
		if exc.errno != errno.EEXIST:
			raise


with open("{}/report_{}.csv".format(output_folder, ts, ts), mode="w+") as csv_file:
	colnames = ["drink", "price", "hour", "arrival_no"]
	writer = csv.DictWriter(csv_file, fieldnames=colnames)
	writer.writeheader()
	for hour in range(PERIOD_IN_HOURS):
		arrived_per_unit_time = sample_customer.calculate_arrivals()
		print("{} customers arrived in time {}".format(
			arrived_per_unit_time, hour + 1))
		for customer in range(arrived_per_unit_time):
			drinks_displayed = vending_one.drinks_displayed
			drink_choice = sample_customer_choice.choose_drink(
				vending_one.display_stock())
			if (vending_one.dispense_drink(drink_choice) == drink_choice) & (drink_choice is not None):
				print("Customer: {} from time: {} chose: {}".format(
					customer + 1, hour + 1, drink_choice))
				print("Drinks left: {}, Cumulative Earnings: {}".format(
					vending_one.current_stock, vending_one.current_earnings))
				writer.writerow(
					{
						"drink": drink_choice, 
						"price": vending_one.stock_list[drink_choice][0], 
						"hour": hour, 
						"arrival_no": customer
					}
				)
			else:
				print("{} was chosen but not available".format(drink_choice))
				writer.writerow(
					{
						"drink": "missed_sale", 
						"price": 0, 
						"hour": hour, 
						"arrival_no": customer
					}
				)
