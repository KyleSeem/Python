Assignment: Chaining Methods

Return to the Bike Assignment and use the chaining method to produce the same outcome.

Example provided in curriculum:
bike1.ride().ride().ride().reverse().displayInfo()

___________________________________________________________
Bike Assignment Instructions:

1. Create a new class called Bike with the following properties/attributes:
    * price
    * max_speed
    * miles

2. Create 3 instances of the Bike class.

3. Use the init() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the init() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

4. Add the following functions to this class:
    * displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
    * ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
    * reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...

5. Have the first instance ride three times, reverse once and have it displayInfo().

6. Have the second instance ride twice, reverse twice and have it displayInfo().

7. Have the third instance reverse three times and displayInfo().

8. What would you do to prevent the instance from having negative miles?
