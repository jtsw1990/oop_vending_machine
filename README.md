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
- run ```python main.py``` to start simulation 

## File Structure


|File/Folder|Description|
|:------|-----:|
|main.py|Main loop that runs the simulation|
|vending_machine|Folder containing vending machin, customer, and reporting scripts|
|analytics|Folder containing sales report outputs|

