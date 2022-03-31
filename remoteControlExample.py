import random
import time

class remoteControl():
    def __init__(self,status = "Closed",soundLevel = 20,channelList = ["Kanal D", "beIN Sports", "S Sports"],channel = "beIN Sports"):
        print("Creating New Smart RC")
        self.status = status
        self.soundLevel = soundLevel
        self.channelList = channelList
        self.channel = channel

    def soundUp(self):
        print("sound Level Increasing...")
        time.sleep(1)
        self.soundLevel = soundLevel + 1
        print("New Sound Level: {}", self.soundLevel)

    def soundDown(self):
        print("Sound Level Decreasing...")
        time.sleep(1)
        self.soundLevel = soundLevel + 1
        print("New Sound Level: {}", self.soundLevel)

    def tvTurnOff(self):
        print("TV Shutting Down...")
        time.sleep(1)
        self.status = "Closed"

    def tvTurnOn(self):
        print("TV Starting...")
        time.sleep(1)
        self.status = "Open"

    def randomChannel(self):
        self.channel = self.channelList[random.randint(0,len(self.channelList)-1)]

    def addChannel(self,newChannel):
        self.channelList.append(newChannel)

    def __str__(self):
        return "TV Status:{} \nSound Level:{}\nChannel List:{}\nChannel:{}".format(self.status,self.soundLevel,self.channelList,self.channel)

    def __len__(self):
        pass


remote_1 = remoteControl()

print(remote_1)

