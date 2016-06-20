#Coding Dojo Python Week 2 Assignment: MathDojo
"""
PART I
Create a Python class called MathDojo that has the methods  add and subtract.
Have these 2 functions take at least 1 parameter.

Then create a new instance called md. It should be able to do the following:
    MathDojo().add(2).add(2, 5).subtract(3, 2).result
which should perform 0+2+(2+5)-(3+2) and return 4.
"""
print "---PART ONE---\n"
class MathDojo(object):
    def __init__(self):
        #each new instance created will start with a value of 0
        self.value = 0
        print "STARTING VALUE: {}".format(self.value)
        #used .format() to allow for easy mod of starting value

    def add(self, *kwargs):
        #*kwargs allows for miltiple (unspecified amount) args
        for arg in kwargs:
            self.value += arg
            print " + {} = {}".format(arg, self.value)
        return self #allows chaining of methods

    def subtract(self, *kwargs):
        for arg in kwargs:
            self.value -= arg
            print " - {} = {}".format(arg, self.value)
        return self

md = MathDojo()
md.add(2).add(2, 5).subtract(3,2)
print "FINAL VALUE: {}".format(md.value)


"""
PART II
Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter
with as many values passed in the list. It should be able to do the following:
    MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25])
    .subtract(2, [2,3], [1.1, 2.3]).result
    should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) & return its result.

PART III
Make any needed changes in MathDojo in order to support tuples of values in
addition to lists and singletons.
"""

print "\n---PART TWO---\n"
#created new class in order to view the differenecs side by side

class MathDojo2(object):
    def __init__(self):
        self.value = 0
        print "STARTING VALUE: {}".format(self.value)

    def add(self, *kwargs):
        for arg in kwargs: #searhces for multiple arguments
            if isinstance(arg, list):
            #checks to see if value is in list format
                for val in arg: #separates each item in list
                    self.value += val
                    print " + {} = {}".format(val, self.value)
            elif isinstance(arg, float):
            #checks to see if value is decimal
                for dec in arg:
                    self.value += dec #allows decimals to be added to value
                    print " + {} = {}".format(dec, self.value)
            else: #any leftover arguments that are neigher floats nor in lists
                self.value += arg
                print " + {} = {}".format(arg, self.value)
        return self

    def subtract(self, *kwargs):
        for arg in kwargs:
            if isinstance(arg, list):
                for val in arg:
                    self.value -= val
                    print " - {} = {}".format(val, self.value)
            elif isinstance(arg, float):
                for dec in arg:
                    self.value -= dec
                    print " - {} = {}".format(dec, self.value)
            else:
                self.value -= arg
                print " - {} = {}".format(arg, self.value)
        return self

md2 = MathDojo2()
md2.add([1],3,4).add([3, 5, 7, 8],[2, 4.3, 1.25]).subtract(2,[2,3],[1.1, 2.3])

print "FINAL VALUE: {}\n".format(md2.value)
