#OOP - creating classes: HUMAN FACTORY!!!
#from __future__ import print_function
import random

class Human(object):
    def __init__(self, clan=None):
        print 'New Human!'
        self.clan = clan
        self.health = 100
        self.stealth = 5
        self.smarts = 5
        self.strength = 5
    def taunt(self):
        print "Ha ha! You smell terrible!"
    def attack(self):
        self.taunt
        luck = round(random.random() * 100)
        if luck > 50:
            if luck * self.stealth >150:
                print "Attacking!!!"
                return True
            else:
                print "Attack Failed!"
                return False
        else:
            self.health -= self.strength
            return False
