class demo:
    def __init__(self):
        self.a=10
        self.b=20
        print("con")
d1=demo()
d2=demo()
print("d1", d1.__dict__)
print("d2", d2.__dict__)
del d1.a
del d2.b
print("d1", d1.__dict__)
print("d2", d2.__dict__)
