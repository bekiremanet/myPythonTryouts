def multiple(x,y):   #  FOR LISTS.
    return x*y

print(list(map(multiple, [2], [3])))

print(list(map(multiple, [0,2,4,6,8],[0,1,3,5,7])))

list_1 = [10,20,30,40,50,60]
list_2 = [45,65,10,5,5,12]

print(list(map(lambda x,y : x/y, list_1, list_2)))