import os
import time
import numpy as np
import matplotlib.pyplot as plt
class PingFinder:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0
        self.average = 0
        self.output = ""
        self.outputlist = []
        self.minlist = []
        self.maxlist = []
        self.avrlist = []
        self.timelist = []

    def TestPing(self,number):
        for x in range(number):
            self.GetPing()
            self.FindPingInfo()
            self.AppendToLists()

    def GetPing(self):
        cmd = "ping www.google.co.uk"
        output_stream = os.popen(cmd)
        self.output = output_stream.read()
        print(self.output)

        
    def FindPingInfo(self):
        bottomRowIndex = self.output.index("Minimum")
        self.FindPingValues(self.output[bottomRowIndex:])

    def FindPingValues(self,bottomRow):
        self.outputlist = []
        valuelist = bottomRow.split(",")
        for item in valuelist:
            for index,letter in enumerate(item):
                if letter == "=":
                    firstIndex = index+2
                if letter == "m" and item[index+1] == "s":
                    lastIndex = index
            self.outputlist.append(item[firstIndex:lastIndex])
        current_time = str(time.gmtime().tm_hour)+":"+str(time.gmtime().tm_min)+":"+str(time.gmtime().tm_sec)
        self.outputlist.append(current_time)

    def AppendToLists(self):
        self.minlist.append(int(self.outputlist[0]))
        self.maxlist.append(int(self.outputlist[1]))
        self.avrlist.append(int(self.outputlist[2]))
        self.timelist.append(self.outputlist[3])

    def DrawGraph(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")
        plt.plot(self.timelist,self.minlist,label="Minimum",color="b")
        plt.plot(self.timelist,self.maxlist,label="Maximum",color="r")
        plt.plot(self.timelist,self.avrlist,label="Average",color="g")
        plt.ylim(bottom=0)
        plt.xlim(left=0)
        plt.xlabel("Time")
        plt.ylabel("Ping")
        plt.legend()
        plt.show()
