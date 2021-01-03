class demo:
    def m1(self):
        print("ok")
    def m2(self):
        print("gh")

class abc(demo):
    def m2(self):
        print("sd")
a=abc()
a.m1()
a.m2()
