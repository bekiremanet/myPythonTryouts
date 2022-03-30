# OVERRIDING 
# Başka bir sınıftan miras alınan methodları kendi sınıfımızda tanımlarsak öncekiler silinir. Overriding.

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
    def __init__(self, name, surname, department, salary, experience): # Overriding
        print("Init functıon of Manager Class")
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary
        self.experience = experience

    def increaseSalary(self, increaseSalary):
        self.salary = self.salary+increaseSalary
        print("New Salary for {} {} : {}".format(self.name, self.surname, self.salary))


manager_1 = Manager("Habib", "Hashemzadeh", "Design", 1000, 10)

