class demo:
    def m1(a):
        print("con")
class sub1(demo):
    def m2(self):
        print("ok")

class sub2(sub1):
    def m3(self):
        print("go")

s=sub2()
s.m1()
s.m2()
s.m3()
