# oop_vending_machine

Simple E2E data project from vending machine simulation to generation of analytics


## Project Summary

The purpose of this project is to get a gentle introduction to Object Oriented Programming (OOP).
This includes tackling concepts of encapsulation, state of an object, interfaces and unit tests.
Note that because learning OOP is the main driver of this project, some elements may seem to be over-engineered when not really required, for example:
- Documentation and comments where not really needed
- Unit tests where not really needed

Premise of the project is the simulation of a typical vending machine dispensing drinks to customers throughout the day.

- The initial stock and unit price of drinks in the vending machine are from a csv
- Customers are assumed to arrive throughout the day following a Poisson(K) distribution, where K is the average number of arrivals per hour
- The script also provides a report of sales at the end of the simulation


## How to use

- git clone this repository into your machine
- run ```pip install -r requirements.txt``` to get dependencies
- open ```config.json``` to set inputs for machine capacity and number of hours to simulate
- open ```./vending_machine/drinks_list.csv``` to define the stock of drinks available at the start
- run ```python main.py``` to start simulation 
- open ```./analytics/dd_mm_yy-hh_mm``` folder to review sales report

## File Structure

|File/Folder|Description|
|:------|-----:|
|main.py|Main loop that runs the simulation|
|config.json| Configuration file containing input variables for max capacity of vending machine, and number of hours to simulate|
|vending_machine|Folder containing vending machin, customer, and reporting scripts|
|analytics|Folder containing sales report outputs|
|test| Folder containing all the unit test scripts. This uses the built-in unittest module|
