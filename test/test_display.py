import unittest
import sys
import os
import csv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vending_machine.vending_machine import VendingMachine, DataReader


class TestingDisplay(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		with open("testing_df.csv", mode="w+") as csv_file:
			colnames = ["name", "price_per_unit", "no_of_units"]
			writer = csv.DictWriter(csv_file, fieldnames=colnames)
			writer.writeheader()
			writer.writerow(
				{"name": "coke", "price_per_unit": 1, "no_of_units": 1})

	@classmethod
	def tearDownClass(cls):
		os.remove("testing_df.csv")


	def testing_display(self):
		test_class = VendingMachine(1)
		test_class.load_drinks("testing_df.csv")
		test_return_1 = test_class.dispense_drink("coke")
		self.assertEqual(test_return_1, "coke", f"Expected coke, {test_return_1} returned.")
		test_return_2 = test_class.dispense_drink("coke")
		self.assertEqual(test_return_2, None, f"Expected None, {test_return_2} returned.")

if __name__ == "__main__":
	unittest.main()
