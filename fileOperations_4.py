# Dosyaların herhangi bir byte'ından başlayıp değişiklik yapmak...

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r+", encoding="utf-8") as file_1: # r+ command
    file_1.seek(16)
    file_1.write("603\n")
    print(file_1.read())


# Dosyaların sonuna bir yazı eklemek. İlk etapta "a" (append) kipiyle dosya açılır...

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "a", encoding="utf-8") as file_1:
    file_1.write("\nLast column of the text.")

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8") as file_1:
    print(file_1.read())

# Dosyaların başında bir değişiklik yapmak.

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r+", encoding="utf-8") as file_1:
    content = file_1.read()
    content = "BOM LIST\n" + content
    file_1.seek(0)
    file_1.write(content)
    print(content)


# Dosyaların ortasında bir değişiklik yapmak. 

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r+", encoding="utf-8") as file_1:
    liste = file_1.readlines() # Dosyanın satırları bir dizi içine atıldı.
    liste.insert(3, "Order: 750\n")
    file_1.seek(0)

    for i in liste:
        print(i, end="")

# Dosyaların ortasında for döngüsü kullanmadan değişiklik yapmak.

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r+", encoding="utf-8") as file_1:
    liste = file_1.readlines()
    liste.insert(3,"Non-order: 1740\n")
    file_1.seek(0)
    file_1.writelines(liste)

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r+", encoding="utf-8") as file_1:
    content = file_1.read()
    print(content)




