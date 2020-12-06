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
				
        print("__init__ was being called here")
        self.filepath = filepath
        self._max_storage = 200
        self._current_earnings = 0
        self._drinks_list = DrinksData(self.filepath).df
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
        
    
    def __repr__(self):
    	print("__repr__ was being called here")
    	return "VendingMachine({!r})".format(self.filepath)
    	
    def __str__(self):
    	pass
    	
    	

    def dispense_drink(self, drink_name):
    		
        '''
			  Receives an string input from customer object
			  that simulates drink choice given what is displayed
			  from the drinks_displayed interface
			  '''
        # TODO: insert test to check index
        # TODO: insert try except bounds
        self._stock_list[drink_name][-1] -= 1
        self._current_earnings += self._stock_list[drink_name][0]


if __name__ == "__main__":
	test_run = VendingMachine("drinks_list.csv")
	print(test_run._stock_list)
	test_run.dispense_drink("coke")
	print(test_run._stock_list)

