#Animal Assignment - Python week 2
"""Create a class called Animal with the following attributes: name, and health.
Give a new animal a health of 100 when it gets created.
Give the animal following three methods: walk, run, and displayHealth.
    When walk() is invoked, have the health decrease by 1.
    When run() is involved, have the health decrease by 5.
    When displayHealth() is invoked, display on screen Animal name and health.

Create an instance of the animal called 'animal'
    Have this animal walk three times, run twice, and display its health.

Create a class called Dog that inherits everything from Animal, BUT:
    Default health is 150 / add new method 'pet' - increases health by 5.
    Have Dog walk() three times, run() twice, pet() once, and displayHealth().

Create a class called Dragon that inherits everything from Animal, BUT
    Default health be 170 / add a new method 'fly' - decreases health by 10.
    Have Dragon walk() three times, run() twice, fly() twice, & displayHealth().
    When Dragon's displayHealth function is called:
        Have it say 'this is a dragon!' before it displays the default
        information (by calling the parent's displayHealth function).
"""
#Parent class
class Animal(object):
    #methods in this class are available to all child classes as well
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self, wgo):
        #walk method removes 1 health per walk
        self.wgo = wgo
        self.health -= self.wgo
        return self

    def run(self, rgo):
        #run method removes 5 health per walk
        self.rgo = rgo
        self.health -= self.rgo*5
        return self

    def displayHealth(self):
        #displays health info after any arguments have been implented
        print "{}'s current health is {}.\n".format(self.name, self.health)

#Sub (Child) classes
class Dog(Animal):
    def __init__(self, name='Pickle'):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self, pets):
        #pet method adds 5 health per pet -- only available to Dog class
        self.pets = pets
        self.health += self.pets*5
        return self

class Dragon(Animal):
    def __init__(self, name='Barnaby'):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self, wings):
        #fly method removes 5 health per fly -- only available to Dragon class
        self.wings = wings
        self.health -= self.wings*5
        return self

    def brag(self):
        #prints for Dragon class only, and only if called
        print "This is a dragon!"
        return self

animal = Animal('Alpha-Animal').walk(3).run(2).displayHealth()
dog = Dog().walk(3).run(2).pet(1).displayHealth()
dragon = Dragon().walk(3).run(2).fly(2).brag().displayHealth()
