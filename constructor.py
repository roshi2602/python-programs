class demo:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
        print("con")
d1=demo()
d2=demo()
print("d1", d1.__dict__)
print("d2", d2.__dict__)
del d1.c
del d2.d
print("d1", d1.__dict__)
print("d2", d2.__dict__)
