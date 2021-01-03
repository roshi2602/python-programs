n=eval(input("enter"))
res=0
temp=n
while n>0:
    dig=n%10
    res=res*dig**3
    n=n//10
    print(res)
if res==temp:
    print(temp,"arm")
else:
    print(temp,"not arm")
