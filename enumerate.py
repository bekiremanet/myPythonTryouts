list_1 = ["x","y","z","t"]

result = list()

i = 0

for a in list_1:
    result.append((i,a))
    i += 1

print(result) # output => [(0, 'x'), (1, 'y'), (2, 'z'), (3, 't')]
 
print(list(enumerate(list_1))) # output => [(0, 'x'), (1, 'y'), (2, 'z'), (3, 't')]

list_2 =["a","b","c","d","e","f"]

for index, element in enumerate(list_2):  # Bir listenin çift indekslerine ait elemanları yazdırmak.
    if(index % 2 == 0):
        print("Element: ", element)  # output => Element:  a\nElement:  c\nElement:  e

