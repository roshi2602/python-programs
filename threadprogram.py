import time
from threading import *
def dou(nos):
    for n in nos:
        time.sleep(3)
        print("ff",2*n)

def sq(nos):
    for n in nos:
        time.sleep(3)
        print("dd",2*n)
num=[1,2,3,4,5]
begintime=time.time()
t1= Thread(target=dou,args=(num,))
t2 = Thread(target =sq, args=(num,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print("Ff",endtime-begintime)
