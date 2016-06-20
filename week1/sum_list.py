#prints the sum of all integers in list a
a = [1,2,5,10,255,3]
x = 0
my_sum = 0
while x < len(a):
    my_sum = my_sum+a[x]
    x = x+1
print my_sum

#or
b = [1,2,5,10,255,3]
print sum(b)
