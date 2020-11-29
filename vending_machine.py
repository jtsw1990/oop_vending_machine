import csv


class DrinksData:
    '''
    Object to read in initial drinks data set
    to be used as input in VendingMachine class
    '''

    def __init__(self, filepath):
        self.df = []
        with open(filepath, "r") as file:
        	my_reader = csv.reader(file, delimiter=",")
        	next(my_reader)
        	for row in my_reader:
        		self.df.append(row)


class VendingMachine:

    '''
    Object to simulate behavior of a vending machine
    '''

    def __init__(self, filepath):

        self._max_storage = 200
        self._current_earnings = 0
        self._drinks_list = DrinksData(filepath).df
        self._stock_list = {
            row[0]: [float(row[1]), int(row[2])]
            for row in self._drinks_list
        }
        # Exposed as interface
        self.drinks_displayed = list(set(self._stock_list.keys()))
        self._current_stock = sum([
            value[-1] for key, value in self._stock_list.items()
        ])
        # TODO: insert try except to assert < max units

    def dispense_drink(self, drink_idx):
				
				'''
				Receives an integer input from customer object
				that simulates drink choice given what is displayed
				from the drinks_displayed interface
				'''
        # TODO: insert test to check index
        # TODO: insert try except bounds
        self._stock_list[self.drinks_displayed[drink_idx]][-1] -= 1
        self._current_earnings += self._stock_list[self.drinks_displayed[drink_idx]][0]


if __name__ == "__main__":
	test_run = VendingMachine("drinks_list.csv")
	#print(test_run._current_stock)
	test_run.dispense_drink(3)

