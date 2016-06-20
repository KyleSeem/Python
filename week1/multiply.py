#function will return list where each integer has been multiplied by 5
def multiply(a,b):
    new_list = []
    for int in a:
        i = int*b
        new_list.append(i)
    return new_list

mine = multiply([2,4,10,16], 5)
print mine
