class demo:
    def __init__(self,age=0):
        self.age=age

    def getage(self):
        return self.age

    def setage(self,x):
        self.age=x

d=demo()
d.setage(34)
print(d.getage())
print(d.age)
