n=eval(input("enter"))
max=9
min=0
temp=n
while n>0:
    dig=n%10
    if max>0:
        max=dig
    if min<0:
        min=dig
    n=n//10
print("ee",max)
print("we",min)
