import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vending_machine import vending_machine.VendingMachine


class TestingStorageBounds(unittest.TestCase):

    def test_max_storage(self):
		vm_instance = VendingMachine("drinks_list.csv")
		total_stock = vm_instance._current_stock
		max_storage = total_stock - 1
		self.assertTrue(
		total_stock <= max_storage, "Stock list exceeds vending machine max storage"
		)
		'''
        with self.assertRaises(ValueError) as exception_context:
            add_fish_to_aquarium(fish_list=too_many_fish)
        self.assertEqual(
            str(exception_context.exception),
            "A maximum of 10 fish can be added to the aquarium"
			'''

			
    def test_min_storage(self):
        pass


if __name__ == "__main__":
    unittest.main()
