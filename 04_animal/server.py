# parent class
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self, w=1):
        self.health -= 1 * w
        return self

    def run(self, r=1):
        self.health -= 5 * r
        return self

    def displayHealth(self):
        print "\n{}'s current health is {}.".format(self.name, self.health)


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.name = name
        self.health = 150

    def getPets(self, p=1):
        self.health += 5 * p
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.name = name
        self.health = 170

    def displayHP(self):
        print "I'M A FREAKING DRAGON!!!"
        self.displayHealth()

    def fly(self, f=1):
        self.health -= 10 * f
        return self

# created instances separately and then created commands - example:
        # animal = Animal('Harold the Cat')
        # animal.walk(3).run(2).displayHealth()

# but also wanted to show how you can chain the instantiation with the commands:
animal = Animal('Harold the Cat').walk(3).run(2).displayHealth()
dog = Dog('Pickles the Dog').walk(3).run(2).getPets(1).displayHealth()
dragon = Dragon('Rupert the Dragon').walk(3).run(2).fly(2).displayHP()
