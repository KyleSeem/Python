#Program simulates tossing a coin 5,000 times.
#Displays how many times the head/tail appears.

from __future__ import division
def tossCoin():
    xTally = 0
    yTally = 0
    c = 1 #tracks number of attempts

    while c <= 5000:
        import random
        random.random()
        random_num = random.random()

        if random_num < .5:
            xTally = xTally+1
            print "Attempt #{}: Tossing coin...It's heads! Current tally is".format(c),xTally,"heads and",yTally,"tails."
            c = c+1
        else:
            yTally = yTally+1
            print "Attempt #{}: Tossing coin...It's tails! Current tally is".format(c),xTally,"heads and",yTally,"tails."
            c = c+1

    xFinal = (xTally/5000)*100
    yFinal = (yTally/5000)*100
    print "After 5000 coin tosses, you averaged",int(round(xFinal)),"% heads and",int(round(yFinal)),"% tails. Thanks for playing!"
tossCoin()
