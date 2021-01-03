import gc
import time
class test:
    def __init__(self):
        print("dd")
    def __del__(self):
        print("ff")
t1=test()
t2=t1
t3=t2
t4=t3
del t1
time.sleep(5)
print("dd")
del t2
del t3
time.sleep(5)
print("ff")
time.sleep(5)
del t4
time.sleep(5)
print("end")
