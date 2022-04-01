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

print("""Smart TV Application\n
Commands:\n
1. Sound Up\n
2. Sound Down\n
3  Turn Off\n
4. Turn On\n
5. Random Channel\n
6. Add Channel\n

Press "q" to exit the menu.
""")

while True:
    command = input("Choose the command:")
    if(command == "q"):
        print("Closing the menu.")
        break
    if(command == "1"):
        remote_1.soundUp()
    elif(command == "2"):
        remote_1.soundDown()
    elif(command == "3"):
        remote_1.tvTurnOff()
    elif(command == "4"):
        remote_1.tvTurnOn()
    elif(command == "5"):
        remote_1.randomChannel()
    elif(command == "6"):
        channels = input("Enter the Channels you want to add, separated by ',':")
        willBeAdded = channels.split(",")
        for i in willBeAdded:
            remote_1.addChannel(i)
        print("Channel list updated successfully.")

