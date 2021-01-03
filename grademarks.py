class stu:
    def __init__(self,name,age):
        self.name="rp"
        self.age=23

    def det(self):
        print("cc", self.name)
        print("cc",self.age)

    def sed(self):
        if self.age>18:
            print("fi")
        elif self.age <60:
            print("dd")
        else:
            print("ss")
name=input("pls")
age=eval(input("enter"))
s1=stu("abc",23)
s1.det()
s1.sed()
