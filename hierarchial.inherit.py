class demo:
    def m1(a):
        print("con")
class semo(demo):
    def m2(self):
        print("fon")
class femo(demo):
    def m3(self):
        print("don")
d1=semo()
d2=femo()
d1.m1()
d1.m2()
d2.m3()
d2.m1()
