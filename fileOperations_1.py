 # The "w" command is used to write to a file that will be opened for the first time. 
 # If it is not used for the first time, the file contents are deleted and overwritten.
 

file_1 = open("C:/Users/Bekir Emanet/Desktop/Yüksek Lisans 2021-2022 Bahar/Python Examples/File Operations/bilgileriGoster.txt","w",encoding="utf-8")

file_1.write("Bekir Emanet\n")

file_1.write("Mechatronics Engineer\n")

file_1.close()

# The "a" command is used to overwrite an existing file.

file_2 = open("C:/Users/Bekir Emanet/Desktop/Yüksek Lisans 2021-2022 Bahar/Python Examples/File Operations/showAllInfos.txt", "a", encoding="utf-8")

file_2.write("Name:\n")

file_2.write("Surname:\n")

file_2.write("Telephone Number: \n")

file_2.close()

#Read a file with "r"

file_2 = open("C:/Users/Bekir Emanet/Desktop/Yüksek Lisans 2021-2022 Bahar/Python Examples/File Operations/showAllInfos.txt", "r", encoding="utf-8")

for i in file_2:
    print(i)

file_2.close()