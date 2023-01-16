import time
class Clock:
    def __init__(self):
        self.start_time = ""
        self.end_time = ""
        self.elapsed_time = 0

    def __str__(self) -> str:
        return str(time.gmtime().tm_hour)+":"+str(time.gmtime().tm_min)+":"+str(time.gmtime().tm_sec)

    def StartTimer(self, length):
        self.start_time = self
        print("The Time started at " + self.start_time)
        self.target_time = length
        self.t1 = time.perf_counter()
       

    def TimeEnded(self):
        self.t2 = time.perf_counter()
        self.elapsed_time += self.t2 - self.t1
        self.t1 = time.perf_counter()
        print(self.elapsed_time,"here")
        if self.elapsed_time <= self.target_time:
            self.end_time = self
            print("The Time ended at " + self.end_time)
            return True
        else:
            return False

