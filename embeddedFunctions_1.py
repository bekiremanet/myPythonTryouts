from functools import reduce

measurement = reduce(lambda x,y : x*y, [12,18,2,3]) # REDUCE FUNCTION

print(measurement)

# ---------------------------------------------------- #

enFazla = max([78,54,78,99,145,556])   # MAX. FUNCTION

print(enFazla)

# ---------------------------------------------------- #

filterFunc = list(filter(lambda x : x % 2  == 0 , [0,2,4,12,54,31,17])) # FILTER FUNCTION

print(filterFunc)

print(type(filterFunc))

# ---------------------------------------------------- #
 
liste_1 = [0,2,4,6,8]
liste_2 = [1,3,5,7,9,11,13]

zipFunc = list(zip(liste_1, liste_2))  # ZIP FUNCTION

print(zipFunc)