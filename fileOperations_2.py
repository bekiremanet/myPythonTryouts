""" EXAMPLE 1

file_1 = open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8")

for i in file_1:
    print(i,end="") #Dosyaları boşluksuz okuma. ""

file_1.close()

"""
""" EXAMPLE 2: read() fonksiyonu sayfanın sonuna kadar okur. 

file_1 = open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8")

content = file_1.read()

print("First Reading Part:\n", content, sep="")

content_2 = file_1.read()

print("Second Reading Part:\n", content_2, sep="")

""" 
""" EXAMPLE 3: readline() fonksiyonu dosyanın sadece bir satırını okur.

file_1 = open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8")

print(file_1.readline()) # Yalnızca ilk satır okundu.

print(file_1.readline()) # Yalnızca ikinci satır okundu.

print(file_1.readline()) # Yalnızca üçüncü satır okundu.

"""

""" EXAMPLE 4: readlines() fonksiyonu dosyanın tüm satırlarını bir dizinin (listenin) içine atar.

file_1 = open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8")

print(file_1.readlines())

file_1.close()

"""







