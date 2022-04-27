list_1 = [0,0,1,1,2,4,5,6,4,7,8]
list_2 = [1,2,4,5,7,8,6]
list_3 = [0,0,0,0,0,0]

print(all(list_1)) # output => false
print(any(list_1)) # output => true

print(all(list_2)) # output => true
print(any(list_2)) # output => true

print(all(list_3)) # output => false
print(any(list_3)) # output => false