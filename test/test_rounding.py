import unittest
import sys
import os
import numpy as np
import csv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vending_machine.vending_machine import VendingMachine, DataReader


class TestingRounding(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		with open("testing_df.csv", mode="w+") as csv_file:
			colnames = ["name", "price_per_unit", "no_of_units"]
			writer = csv.DictWriter(csv_file, fieldnames=colnames)
			writer.writeheader()
			writer.writerow({"name": "coke", "price_per_unit": 1.1, "no_of_units": 200})
		
	@classmethod
	def tearDownClass(cls):
		os.remove("testing_df.csv")
		
			
	def test_rounding_earnings(self):
		scenario = VendingMachine(200)
		scenario.load_drinks("testing_df.csv")
		for output in range(200):
			scenario.dispense_drink("coke")
			self.assertEqual(np.round(scenario.current_earnings, 2), scenario.current_earnings)
	
		


if __name__ == "__main__":
	unittest.main()
