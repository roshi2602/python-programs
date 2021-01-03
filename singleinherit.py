class demo:
    def m1(a):
        print("con")
class sub(demo):
    def m2(self):
        print("df")
s=sub()
s.m1()
s.m2()
