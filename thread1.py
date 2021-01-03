from threading import *
import time
def dis():
    for i in range(10):
        print("ct")
t= Thread(target=dis)
t.start()
time.sleep(3)
for i in range(10):
    print("mt")
