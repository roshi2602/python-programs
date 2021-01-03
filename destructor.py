import gc
import time
class test:
    def __init__(self):
        print("ok")
    def __del__(self):
        print("of")
t=test()
time.sleep(1)
t = None
print("end")
