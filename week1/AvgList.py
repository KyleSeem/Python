#prints the average of the values in the list below
a = [1,2,5,10,255,3]
x = 0
my_sum = 0

while x < len(a):
    my_sum = my_sum + a[x]
    x = x + 1
my_avg =my_sum/len(a)
print my_avg

#or

b = [1,2,5,10,255,3]
print sum(b)/len(b)
