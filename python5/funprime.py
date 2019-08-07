def prime(r):
    x=0
    for i in range (2,n+1):
        if n%i==0:
            x=1
        break
    if x==0:
        print("prime")
    else:
        print("not prime")
#---------------------------------------------
n=int(input("enter the number"))
prime(n)
prime(n)
prime(n)

