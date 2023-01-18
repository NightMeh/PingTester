from pingFinder import PingFinder

def RunPingFinder(number):
    pingFinder = PingFinder()
    pingFinder.TestPing(number)
    print(pingFinder.peakdict)
    pingFinder.DrawGraph()
