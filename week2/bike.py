#from __future__ import print_function
import random
#Create a class called Bike with attributes: price, max_speed, miles
#Create 3 instances of the Bike class.
"""Use the __init__() function to specify price and max_speed of each instance
(e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that
the initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:
displayInfo() - display the bike's price, max speed, and total miles.
ride() - display "Riding" on the screen and increase total miles ridden by 10
reverse() - display "Reversing" on the screen and decrease total miles by 5

Have the first instance ride three times, reverse once and displayInfo().
Have the second instance ride twice, reverse twice and displayInfo().
Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?"""

class Bike(object):
    def __init__(self, name, price, max_speed):
        # init requires new instance to define all arguments except miles
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        #displays name, price, max_speed and current miles for each instance
        print "{} is priced at {} with a top speed of {} and a lifetime mileage of {}.".format(self.name,self.price,self.max_speed,self.miles)

    def ride(self, forward):
        #displays name and 1 "Riding..." for each time ridden;
        #increases lifetime miles by 10 per ride
        print ("{}...".format(self.name)*1),("Riding..."*forward)
        self.forward = forward
        self.miles += self.forward*10

    def reverse(self, back):
        #displays name and 1 "Reversing..." for each time reversed;
        #decreases lifetime mileage by 5 per reverse;
        #if statement keeps lifetime mileage from going into negative mileage
        print ("{}...".format(self.name)*1),("Reversing..."*back)
        self.back = back

        if self.miles <= 0:
            self.miles = self.miles
        else:
            self.miles -= self.back*5

#creation of 3 new bikes
bike1 = Bike('Bike 1', '$500', '35mph')
bike2 = Bike('Bike 2', '$50', '5mph')
bike3 = Bike('Bike 3', '$327', '20mph')

#displays starting info for each bike
bike1.displayInfo()
bike2.displayInfo()
bike3.displayInfo()

#bike1: ride*3, reverse*1, display updated info
bike1.ride(3)
bike1.reverse(1)
bike1.displayInfo()

#bike2: ride*2, reverse*2, display updated info
bike2.ride(2)
bike2.reverse(2)
bike2.displayInfo()

#bike3: reverse*3, display updated info
bike3.reverse(3)
bike3.displayInfo()
