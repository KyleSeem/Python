print 'Initial function:'
#Part 1:
#Function takes a list and prints corresponding amount of * for each integer

x = [4,6,1,3,5,7,25]

def draw_stars(x):
    for int in x:
        print '*' * int
draw_stars(x)

print 'Modified function:'
#Part 2:
#Function modified to accept integers and strings

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars2(y):
    for item in y:
        if isinstance(item, int): #determines if integer
            print '*'*int(item)
        elif isinstance(item, str): #determines if string
            print item[0].lower()*len(item) #prints first letter of string * string length
draw_stars2(y)
