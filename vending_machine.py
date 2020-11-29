import pandas as pd


class DrinksData:
    '''
    Object to read in initial drinks data set
    to be used as input in VendingMachine class
    '''

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)


class VendingMachine:

    '''
    Object to simulate behavior of a vending machine
    '''

    def __init__(self, filepath):

        self._max_storage = 200
        self._current_earnings = 0
        self._drinks_list = DrinksData(filepath).df
        self._stock_list = {
            row["name"]: [row["price_per_unit"], row["no_of_units"]]
            for index, row in self._drinks_list.iterrows()
        }
        self.drinks_displayed = list(set(self._drinks_list["name"]))
        self._current_stock = sum([
            value[-1] for key, value in self._stock_list.items()
        ])
        # TODO: insert try except to assert < max units

    def dispense_drink(self, drink_name):

        # TODO: insert test to check index
        # TODO: insert try except bounds
        self._stock_list[drink_name][-1] -= 1
        self._current_earnings += self._stock_list[drink_name][0]


if __name__ == "__main__":
    vending_one = VendingMachine("drinks_list.csv")
    vending_one.dispense_drink("coke")
    print(vending_one._stock_list)
    print(vending_one._current_earnings)
    vending_one.dispense_drink("fanta_grape")
    print(vending_one._stock_list)
    print(vending_one._current_earnings)
