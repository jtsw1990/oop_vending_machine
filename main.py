from vending_machine import DrinksData, VendingMachine
from customer_simulation import CustomerArrival, CustomerChoice


vending_one = VendingMachine("drinks_list.csv")
customer_options = CustomerChoice(sum(vending_one.drinks_displayed))



