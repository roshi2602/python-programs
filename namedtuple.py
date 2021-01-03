from collections import namedtuple
student = namedtuple("student",["name","roll","marks"])
stu1 = student("dug",101,70)
print(stu1.name)
print(stu1.roll)
print(stu1.marks)
