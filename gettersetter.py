class stu:
    def setname(self,name):
        self.name=name
    def getname(self):
        return name
    def selfmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return marks

n=int(input("enter"))
for i in range(n):
    name=input("pls")
    marks=int(input("seb"))
    s=stu
    s.setname(name)
    s.setmarks(marks)
    s=stu(name, marks)
    print("hi",s.getname())
    print("si",s.getmarks())
    print("*"*15)
