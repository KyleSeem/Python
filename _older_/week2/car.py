import random

"""Create a class called Car. In the__init__(), allow the user to specify the
following attributes: price, speed, fuel, mileage. If the price is greater than
10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

Create five different instances of the class Car. In the class have a method
called display_all() that returns all information about the car as a string.
In your __init__(), call this display_all() method to display information about
the car once the attributes have been defined.
A sample output would be like this:

Price: 2000
Speed: 35mph
Fuel: Full
Mileage: 15mpg
Tax: 0.12
"""

class Car(object):
    def __init__(self, name, price, speed, fuel, mileage):
        #init requires new isntance to define all arguments except tax
        #if statement determines tax rate based on price
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15

        self.display_all()
        #calls display_all function with the creation of new instances

    def display_all(self):
        #displays specs for each instance in a single string;
        #new line for each spec, all arguments inserted with {}.format()
        print "{}\nPrice: ${}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}\n".format(self.name,self.price,self.speed,self.fuel,self.mileage,self.tax)

#creation of 5 new cars in class Car
car1 = Car('Red Car', 6000, '65mph', 'Full', '24mpg')
car2 = Car('Orange Car', 2000, '35mph', 'Half-Full', '15mpg')
car3 = Car('Yellow Car', 8000, '85mph', 'Half-Empty', '22mpg')
car4 = Car('Green Car', 4000, '50mph', 'Empty', '36mpg')
car5 = Car('Blue Car', 20000, '120mph', 'Full', '8mpg')
