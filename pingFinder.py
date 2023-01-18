import os
import numpy as np
import matplotlib.pyplot as plt
from clock import Clock
import seaborn as sns
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
        self.clock = Clock()
        self.current_total = 0
        self.current_numberofchecks = 0
        self.peaklist = []
        self.MODIFIER = 2
        self.peakdict = {
            "Time":[],
            "Ping":[]
        }


    def TestPing(self,number):
        self.clock.StartTimer(number)
        self.current_total = 0
        self.current_numberofchecks = 0
        while not(self.clock.TimeEnded()):
            self.GetPing()
            try:
                self.FindPingInfo()
                self.AppendToLists()
            except ValueError:
                print("Request Time Out")

    def GetPing(self):
        cmd = "ping www.google.co.uk"
        output_stream = os.popen(cmd)
        self.output = output_stream.read()

        
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
        current_time = self.clock
        self.outputlist.append(str(current_time))

    def AppendToLists(self):
        self.current_numberofchecks += 1
        self.minlist.append(int(self.outputlist[0]))
        self.maxlist.append(int(self.outputlist[1]))
        self.avrlist.append(int(self.outputlist[2]))
        self.timelist.append(self.outputlist[3])
        self.current_total += int(self.outputlist[2])
        if self.CheckValueAboveAverage(int(self.outputlist[1])):
            self.peakdict["Time"].append(self.outputlist[3])
            self.peakdict["Ping"].append(self.outputlist[1])


    def CheckValueAboveAverage(self,value):
        if value >= (self.current_total/self.current_numberofchecks)*self.MODIFIER and value != self.avrlist[0]:
            return True
        else:
            return False


    def DrawGraph(self):
        outputdict = {}
        outputdict["Minimum"] = self.minlist
        outputdict["Average"] = self.avrlist
        outputdict["Maximum"] = self.maxlist
        outputdict["Time"] = self.timelist
        sns.set_theme(style="ticks")
        sns.lineplot(data=outputdict,x="Time", y="Maximum")
        sns.lineplot(data=outputdict,x="Time", y="Average")
        sns.lineplot(data=outputdict,x="Time", y="Minimum")
        plt.ylim(bottom=0,top=300)
        plt.xlim(left=0)
        plt.show()
