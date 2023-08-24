# Coffee-Vending-Machine-Simulation
A console based simulation that attempts to mimic the key properties of a Coffee Vending Machine.


Program Key Requirements/Properties as instructed by instructor:
1. Print vending machine profit report
2. Check for resources within vending machine if sufficient
3. Proccess coins given/inputted by user
4. Check to see if transaction was successful, return any change necessary
5. Make hot coffee selected

## What was learned/practiced
With this project the main subject was Objects and Classes,<br>
you may notice within this project there is 2 main.py files, one holds an "Iterative Programming" approach to this assignment and the other wthin the "\OOP Coffee Machine" directory holds an "Object Oriented Programming" approach.
<br>
<br>

The program composes of 3 main Classes: 
1. Menu
2. MoneyMachine
3. CoffeeMaker
   
### Class: Menu
This class is responsible for modeling the menu in the console.
<br>
The class is composed of 2 methods: .get_items() and .find_drink()
<br>

### Class: MoneyMachine
This class is resonsible for processing money inserted (in coin format) and making the transaction within the vending machine. Within this class was also placed the profit report feature which returns the total amount of money that has been processed.
<br>
This class is composed with 3 methods: .report(), .process_coin(), and .make_payment()
<br>

### Class: CoffeeMaker
This class is responsible for managing the resources within the vending machine and crating the coffee with the available resouces, if not enough resources in vending machine, user will be prompted. In this class you will notice another "report()" method, this one in spcifically works in conjunction with the other "report()" in the "Money Machine" class, this report in specifically return the remaming resources within the vending machine.
<br>
This class is composed of 3 methods: .report(), is_resource_sufficient(), make_coffee()
<br>
