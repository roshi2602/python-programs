class Too(Exception):
    def __init__(self,age):
        self.age=age
class Tyo(Exception):
    def __init__(self,age):
        self.age=age
age=int(input("enter"))
if age<18:
    raise Too("now")
elif age>62:
    raise Tyo("gt")
else:
    print("thanks")
