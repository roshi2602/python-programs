n=int(input("enter"))
sum=0
for i in range(1,n+1//2):
    if n%i==0:
        sum=sum+i
    if sum==n:
        print(n,"perfect")
    else:
        print(n,"not perfect")
