import unittest
import sys
import os
import numpy as np
import csv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vending_machine.vending_machine import VendingMachine, DataReader


class TestingCapacty(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		with open("testing_df.csv", mode="w+") as csv_file:
			colnames = ["name", "price_per_unit", "no_of_units"]
			writer = csv.DictWriter(csv_file, fieldnames=colnames)
			writer.writeheader()
			writer.writerow({"name": "coke", "price_per_unit": 1, "no_of_units": 500})
		
	@classmethod
	def tearDownClass(cls):
		os.remove("testing_df.csv")


	def test_capacity_input(self):
		for scenario in np.linspace(-2, 2, 9):
			if scenario < 0:
				self.assertRaises(ValueError, VendingMachine, scenario)
			elif scenario % 1 != 0:
				self.assertRaises(TypeError, VendingMachine, scenario)
			else:
				self.assertEqual(scenario, VendingMachine(scenario).max_capacity)

	def test_capacity_bound(self):
		scenario = VendingMachine(200)
		self.assertRaises(ValueError, scenario.load_drinks, "testing_df.csv")


if __name__ == "__main__":
	unittest.main()

