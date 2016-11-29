
class Bike(object):
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "-" * 50
        print "{} is priced at {}, has a top speed of {} and has a current mileage of {}.\n".format(self.name, self.price, self.max_speed, self.miles)
        return self

    def ride(self, forward):
        # print ("{} is...".format(self.name), "Riding..." * forward)
        print "Riding..." * forward
        self.forward = forward
        self.miles += forward * 10
        return self

    def reverse(self, backward):
        print "Reversing..." * backward
        self.backward = backward
        if self.miles <= 0:
            self.miles = self.miles
        else:
            self.miles -= backward * 5
        return self

    def update(self):
        # updates and prints mileage without repeating other class specs
        print "\nUpdated Mileage: {}".format(self.miles)
        print "-" * 50
        return self

    def declare(self):
        # removed name from ride/reverse print statement and declare in new method so neame isn't repeated
        print "{} is...".format(self.name)
        return self

# create 3 new instances of class Bike
bike1 = Bike('Red Bike', '$600', '40mph')
bike2 = Bike('Blue Bike', '$75', '10mph')
bike3 = Bike('Yellow Bike', '$399', '25mph')

# use chaining method to give all instructions to instance in single line
    # bike1 = ride*3, reverse*1, display
    # bike2 = ride*2, reverse*2, display
    # bike3 = reverse*3, display

bike1.displayInfo().declare().ride(3).reverse(1).update()
bike2.displayInfo().declare().ride(2).reverse(2).update()
bike3.displayInfo().declare().reverse(3).update()
