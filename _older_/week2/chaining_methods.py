#Go back to the Bike assignment and change it to allow chaining of methods
#Use return self to chain methods more efficiently

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
        return self
    def ride(self, forward):
        #"Riding..." for each time ridden;
        #increases lifetime miles by 10 per ride
        print ("Riding..."*forward)
        self.forward = forward
        self.miles += self.forward*10
        return self

    def reverse(self, back):
        #"Reversing..." for each time reversed;
        #decreases lifetime mileage by 5 per reverse;
        print ("Reversing..."*back)
        self.back = back

        #if statement keeps lifetime mileage from going into negative mileage
        if self.miles <= 0:
            self.miles = self.miles
        else:
            self.miles -= self.back*5
        return self

    def updateMiles(self):
        #prints updated mileage without including all other specs in display
        print "Updated mileage: {}.\n".format(self.miles)


#creation of 3 new bikes
bike1 = Bike('Bike 1', '$500', '35mph')
bike2 = Bike('Bike 2', '$50', '5mph')
bike3 = Bike('Bike 3', '$327', '20mph')

#bike1: display starting info, ride*3, reverse*1, display updated info
bike1.displayInfo().ride(3).reverse(1).updateMiles()

#bike2: display starting info, ride*2, reverse*2, display updated info
bike2.displayInfo().ride(2).reverse(2).updateMiles()

#bike3: display starting info, reverse*3, display updated info
bike3.displayInfo().reverse(3).updateMiles()
