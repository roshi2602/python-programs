from threading import *
import time
def dis():
    print("cc",current_thread().name)
    time.sleep(3)
print("dd", active_count())
t1= Thread(target = dis,name="c1")
t2 = Thread(target = dis, name="c2")
t1.start()
t2.start()
print(t1.name, "is", t1.is_alive())
print(t2.name,"is", t2.is_alive())
print()
