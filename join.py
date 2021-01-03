from threading import *
import time
def dis():
    for i in range(10):
        print("ct")
        time.sleep(3)
t=Thread(target = dis)
t.start()
t.join()
for i in range(10):
    print("mt")
