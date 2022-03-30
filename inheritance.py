# INHERITANCE (KALITIM)
# Bir class'a ait objelere, diğer bir class'ın da ulaşıp kullanabilmesi. Miras alması.

import time
import random

class Colleague():
    def __init__(self,name,surname,department,salary):
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

    def showInfos(self):
        print("Showing Infos...")
        time.sleep(2)
        print("Name: {}\nSurname: {}\nDepartment: {}\nSalary: {}".format(self.name,self.surname,self.department,self.salary))

    def changeDepartment(self, newDepartment):
        self.department = newDepartment

class Manager(Colleague): # Inheritance
    def increaseSalary(self, increaseSalary):
        self.salary = self.salary+increaseSalary
        print("New Salary for {} {} : {}".format(self.name, self.surname, self.salary))

manager_1 = Manager("Bekir", "Emanet", "Mechatronics", 100)

manager_1.showInfos()
#manager_1.changeDepartment("Electronics")
#manager_1.showInfos()
manager_1.increaseSalary(500)
