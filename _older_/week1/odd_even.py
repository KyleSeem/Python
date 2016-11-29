#loop generates each number in range and indicates if odd or even
def odd_even(x,y):
    for int in range(x, y):
        while x <= y:
            if x % 2 == 0:
                print 'Number is {}. This is an even number.'.format(x)
                x = x + 1
            elif x % 2 != 0:
                print 'Number is {}. This is an odd number.'.format(x)
                x = x + 1
print odd_even(1,2000)
