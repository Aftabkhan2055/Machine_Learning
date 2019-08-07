def prime(s):
    x=0
    for i in range (2,s+1):
        if s%i==0:
            x=1
        break
    if x==0:
        print("prime")
#---------------------------------------
n=int(input("enter the no "))
prime(n)
