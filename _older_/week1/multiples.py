#prints each odd integer on separate line
x = 1
for int in range(1, 1000):
    if x < 1000:
        print x
        x = x+2

# #prints each odd integer in a single list
my_list = []
y = 1
for int in range(1, 1000):
    if y < 1000:
        my_list.append(x)
        y = y+2

print my_list

#prints all multiples of 5 between 5 and 1,000,000 on a separate line
a = 5
for int in range(5, 1000000):
    if a <= 1000000:
        print a
        a = a+5

#prints all multiples of 5 between 5 and 1,000,000 in a single list
big_list = []
b = 5
for int in range(5, 1000000):
    if b <= 1000000:
        big_list.append(b)
        b = b+5
print big_list
