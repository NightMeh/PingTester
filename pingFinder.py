import os
class PingFinder:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0
        self.average = 0
        self.output = ""

    def GetPing(self):
        cmd = "ping www.google.co.uk"
        output_stream = os.popen(cmd)
        self.output = output_stream.read()
        print(self.output)

        
    def FindPingFromWord(self,word):
        minimum_letterDifference = 0
        lenword = len(word)
        for index,letter in enumerate(self.output):
            if self.output[index:index+lenword] == word:
                while self.output[index+minimum_letterDifference] != "m":
                    minimum_letterDifference += 1
                return self.output[index+3+lenword:index+lenword+1+minimum_letterDifference]

    def OutputToValues(self):
        self.minimum = self.FindPingFromWord("Minimum")
        self.maximum = self.FindPingFromWord("Maximum")
        self.average = self.FindPingFromWord("Average")
        print(self.minimum,self.maximum,self.average)
