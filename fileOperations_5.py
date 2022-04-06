def calculateGrade(column):
    
   # column = column[:-1]  # \n'i pasif duruma getirdi. Satırlararası boşluk yok.

    list_1 = column.split(",")  

    name = list_1[0]
    grade_1 = int(list_1[1])
    grade_2 = int(list_1[2])
    grade_3 = int(list_1[3])

    last_grade = grade_1 * (3/10) + grade_2 * (3/10) + grade_3 * (4/10)

    if (last_grade >= 90):

        textGrade = "AA"
    elif (last_grade >= 85):
        textGrade = "BA"
    elif (last_grade >= 80):
        textGrade = "BB"
    elif (last_grade >= 75):
        textGrade = "CB"
    elif (last_grade >= 70):
        textGrade = "CC"
    elif (last_grade >= 65):
        textGrade = "DC"
    elif (last_grade >= 60):
        textGrade = "DD"
    elif (last_grade >= 55):
        textGrade = "FD"
    else:
        textGrade = "FF"
        

    return name + "------------------> " + textGrade + "\n"



file_2 = open("C:/Users/b.emanet/Desktop/dosya_2.txt", "a", encoding="utf-8")

with open("C:/Users/b.emanet/Desktop/dosya.txt", "r", encoding="utf-8") as file_1:

    for i in file_1:

        file_2.write(calculateGrade(i))
        
                
      

    



            