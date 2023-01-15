import time
from pingFinder import PingFinder

pingFinder = PingFinder()
pingFinder.GetPing()
pingFinder.OutputToValues()
current_time = str(time.gmtime().tm_hour)+":"+str(time.gmtime().tm_min)




