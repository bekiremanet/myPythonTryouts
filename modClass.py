import time
import random

class partProperty():
    def __init__(self,bolts,color,material,price):
        self.bolts = bolts
        self.color = color
        self.material = material
        self.price = price
    
    def showInfos(self):
        print("Bolt Type:{}, Part Color:{}, Material Type:{}, price:{}".format(self.bolts,self.color,self.material,self.price))
    
    def increasePrice(self, incRate):
        self.price = self.price + incRate
        print("Increasing price...")
        time.sleep(1)
        print("Bolt Type:{}, Part Color:{}, Material Type:{}, price:{}".format(self.bolts,self.color,self.material,self.price))


motorMount = partProperty("allen","blue", "6061", 1400)

motorMount.showInfos()

motorMount.increasePrice(10)