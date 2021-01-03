from threading import *
class cthread(Thread):
    def run(self):
        for i in range(10):
            print("ct")
ob =cthread()
t= Thread(target =ob.run)
t.start()
for i in range(10):
    print("mt")
