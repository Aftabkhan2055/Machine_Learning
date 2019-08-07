n=int(input("enter the no"))
x=0
for i in range(2,n):
    if n%i==0:
        x=0
        break
    

if x==0:
    print("prime")
else:
    print("not prime")
