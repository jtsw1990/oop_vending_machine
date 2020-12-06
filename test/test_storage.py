import unittest
import sys
import os
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vending_machine.vending_machine import VendingMachine, DataReader


class TestingCapacty(unittest.TestCase):
	
	def test_capacity_input(self):
		for scenario in np.linspace(-2, 2, 9):
			if scenario < 0:
				self.assertRaises(ValueError, VendingMachine, scenario)
			elif scenario % 1 != 0:
				self.assertRaises(TypeError, VendingMachine, scenario)
			else:
				self.assertEqual(scenario, VendingMachine(scenario).max_capacity)
				
	def test_capacity_bound(self):
		# TODO: create csv to for negative test case
		pass
		


if __name__ == "__main__":
	unittest.main()
