# Dosyaları işimiz bittiğinde kapatan özellik.

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8") as file_1:
    for i in file_1:
        print(i)

# Dosyaları ileri-geri sarmak. SEEK ve TELL

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8") as file_1:
    print(file_1.tell()) # TELL fonksiyonu dosyada kaçıncı byte'da olduğumuzu söyler. (0)
    file_1.seek(20) # İmleci 20. byte'a götürdük.
    print(file_1.tell()) 

with open("C:/Users/b.emanet/Desktop/datasheet.txt", "r", encoding="utf-8") as file_1:
    file_1.seek(5)
    content = file_1.read(15) # 15 byte okuma yaptık.
    print(content)
    print(file_1.tell())



