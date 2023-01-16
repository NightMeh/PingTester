from pingFinder import PingFinder

def RunPingFinder():
    pingFinder = PingFinder()
    pingFinder.TestPing(40)
    print(pingFinder.peaklist)
    pingFinder.DrawGraph()
