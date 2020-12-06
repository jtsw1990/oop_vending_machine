import unittest
import sys
import os
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vending_machine.vending_machine import VendingMachine, DataReader


class TestingStorageBounds(unittest.TestCase):
	
	def test_capacity_input(self):
		self.assertRaises(TypeError, 1 + "str")
				
		#test_instance = VendingMachine(150)
		#max_capacity = test_instance.max_capacity
		#self.assertEqual(isinstance(max_capacity, (int, float)), True)


if __name__ == "__main__":
	unittest.main()
	
