class demo:
    def m1(self):
        print("ok")
class sub:
    def m2(self):
        print("to")
class multi(demo,sub):
    def m3(self):
        print("pl")
m=multi()
m.m1()
