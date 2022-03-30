# SUPER 
# Override edilen bir metodun içinde aynı zamanda miras aldığımız bir metodu kullanmak istersek kullanılabilir.
# Miras alınan sınıfın metotlarını alt sınıflardan kullanmaya olanak sağlar.

import time
import random

class Colleague():
    def __init__(self,name,surname,department,salary):
        print("Init functıon of Colleague Class")
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

class Manager(Colleague):
    def __init__(self, name, surname, department, salary, experience): 
        super().__init__(name, surname, department,salary)  # Super (Tüm argümanlar yazılmalı. 4/4)
        print("Init functıon of Manager Class")
        self.experience = experience
    def increaseSalary(self, increaseSalary):
        self.salary = self.salary+increaseSalary
        print("New Salary for {} {} : {}".format(self.name, self.surname, self.salary))

manager_1 = Manager("name", "surname", "department", 1000, 5)

print(manager_1.experience) # Sonradan eklenen metod. 