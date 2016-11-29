class Bike(object):
    def __init__(self, name, price, max_speed):
        # defining all arguments except miles for new instances
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        # displays name, price, max_speed and current mileage for each instance
        print "-"*50
        print "{} is priced at {}, has a top speed of {} and has a current mileage of {}.".format(self.name, self.price,
        self.max_speed, self.miles)
        print "-"*50

    def ride(self, forward):
        # displays phrase "Riding..." and adds 10 miles to current mileage per times ridden
        print ("{} is...".format(self.name)), ("Riding... " * forward)
        self.forward = forward
        self.miles += forward * 10

    def reverse(self, backward):
        # displays phrase "Reversing..." and deletes 5 miles from current mileage per times reversed
        print ("{} is...".format(self.name)), ("Reversing... " * backward)
        self.backward = backward

        # keeps current mileage from going into negative numbers
        if self.miles <= 0:
            self.miles = self.miles
        else:
            self.miles -= backward * 5

# creation of 3 new instances of Bike class
bike1 = Bike('Red Bike', '$600', '40mph')
bike2 = Bike('Blue Bike', '$75', '10mph')
bike3 = Bike('Yellow Bike', '$399', '25mph')

# displays starting info
bike1.displayInfo()
bike2.displayInfo()
bike3.displayInfo()

# bike1 instructions: ride*3, reverse*1, display
bike1.ride(3)
bike1.reverse(1)
bike1.displayInfo()

# bike2 instructions: ride*2, reverse*2, display
bike2.ride(2)
bike2.reverse(2)
bike2.displayInfo()

# bike3 instructions: reverse*3, display
bike3.reverse(3)
bike3.displayInfo()
