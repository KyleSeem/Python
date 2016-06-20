#Coding Dojo Python Week 2 Assignment: Underscore
"""
Create methods from the underscore library as methods of the "_" object.
Pay attention to what you have to change, in terms of parameters for each
method as well as implementation.

Assignment: implement the 5 methods (below) using delegating callbacks.
Modify the 5 methods to take in an array and a callback.
"""

class Underscore(object):
    def map(self, arr, func):
        arrNew = []
        for item in arr:
            arrNew.append(func(item))
        return arrNew

    def reduce(self, arr, func, value=0):
        for item in arr:
            value += func(item)
        return value

    def find(self, arr, func):
        for item in arr:
            if func(item) == True:
                return item

    def filter(self, arr, func):
        arrNew = []
        for item in arr:
            if func(item) == True:
                arrNew.append(item)
        return arrNew

    def reject(self, arr, func):
        arrNew = []
        for item in arr:
            if func(item) == False:
                arrNew.append(item)
        return arrNew

#Create new instance
_ = Underscore()

a = [1,2,3,4,5,6,7,8,9,10] #test list

#Defining one function to illustrate diff between calling func and using lambda
#will only use lambda after first example
def square(x):
    return x ** 2

#Use map to obtain a new list of values based on original list and func called
squares = _.map(a, square) #calls map with predefined function
squarez = _.map(a, lambda x: x**2) #calls map using lambda
print "map:", squares
print "map:", squarez

#Use reduce to sum all integers from list
sumz = _.reduce(a, lambda x: + x)
print "reduce:", sumz

#Use find to locate the first item in list that meets specified criteria
findz = _.find(a, lambda x: x - 2 == 3)
print "find:", findz

#Use filter to collect all items from list that meet specified criteria
filterz = _.filter(a, lambda x: x % 2 == 0)
print "filter:", filterz

#Use reject to collect all items from list that do NOT meet specified criteria
rejectz = _.reject(a, lambda x: x % 2 == 0)
print "reject:", rejectz
