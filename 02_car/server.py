
class Car(object):
    def __init__(self, name, price, speed, fuel, mileage):
        # creates new instance and defines all arguments except tax
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        # define tax requirements
        if self.price >= 10000:
            self.tax = 15
        else:
            self.tax = 12

        # calls display method as soon as a new instance is created
        self.display_all()

    def display_all(self):
        # displays info for each instance of class Car
        print "-"*50
        print "{}\n  Price: ${}\n  Speed: {}\n  Fuel: {}\n  Mileage: {}\n  Tax: {}%".format(self.name, self.price, self.speed, self.fuel, self.mileage, self.tax)


# define 6 instances of Car class
car1 = Car('Red Car', 17000, '140mph', 'Full', '28mpg')
car2 = Car('Orange Car', 7000, '85mph', 'Empty', '36mpg')
car3 = Car('Yellow Car', 4000, '55mph', '3/4 Full', '22mpg')
car4 = Car('Green Car', 3600, '50mph', '1/2 Full', '18mpg')
car5 = Car('Blue Car', 11500, '120mph', 'Full', '34mpg')
car6 = Car('Purple Car', 2500, '60mph', '1/4 Full', '33mpg')
