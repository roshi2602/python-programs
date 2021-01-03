class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class stu(person):
    def __init__(self,name,age,roll,marks):
        super().__init__(name,age)
        self.roll=roll
        self.marks = marks
class tec(person):
    def __init__(self,name,age,sal,sub):
        super().__init__(sal,sub)
        self.sal = sal
        self.sub = sub
s = stu("xd",23,90,45)
t = tec("sd",34,340000,"eng")
