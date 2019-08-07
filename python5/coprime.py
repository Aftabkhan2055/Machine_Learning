def prime(n):
    x=0
    for i in range (2,n+1):
        if n%i==0:
            x=1
        break
    if x==0:
        return "true"
    else:
        return "false"
#----------------------------------------------------------
for i in range (1,101):
    if prime(i) and prime(i+2)=="true":
        print(i,i+2)
