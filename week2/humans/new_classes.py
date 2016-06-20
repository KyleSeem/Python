#sub-classes derived from class Human
import sys
# print sys.path
sys.path.append('C:\\Users\\Kyle\\Desktop\\Coding_Dojo\\Python\\week2')
from humans import Human

class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()
        self.smarts = 15
    def heal(self):
        self.health += 10

class Squib(Human):
    def __init__(self):
        super(Squib, self).__init__()
        self.stealth = 25
    def blend(self):
        self.stealth += 5

class Muggle(Human):
    def __init__(self):
        super(Muggle, self).__init__()
        self.strength = 20
    def baffled(self):
        self.smarts -= 5


harry = Wizard()
arabella = Squib()
dudley = Muggle()

print "Harry: health = {}; stealth = {}; smarts = {}; strength = {}".format(harry.health, harry.stealth, harry.smarts, harry.strength)
print "Arabella: health = {}; stealth = {}; smarts = {}; strength = {}".format(arabella.health, arabella.stealth, arabella.smarts, arabella.strength)
print "Dudley: health = {}; stealth = {}; smarts = {}; strength = {}".format(dudley.health, dudley.stealth, dudley.smarts, dudley.strength)

harry.heal()
print harry.health

arabella.blend()
print arabella.stealth

dudley.baffled()
print dudley.smarts
