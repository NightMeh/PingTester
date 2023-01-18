import time
t1 = time.gmtime().tm_sec
time.sleep(5)
t2 = time.gmtime().tm_sec

t3 = t2-t1
print(t3)