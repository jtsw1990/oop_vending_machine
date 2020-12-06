import csv
from vending_machine import DrinksData


report_id = "06-12-20_13-26"

df = DrinksData("./analytics/{}/report_{}.csv".format(report_id, report_id)).df



