def pal (n):
    rev=""
    for i in range(len(n)-1,-1,-1):
        rev=rev+n[i]
    if rev==n:
        return "true"
    else:
        return "false"


#-----------------------------------------------
def prime(n):
    x=0
    for i in range (2,n+1):
        if n%i==0:
            x=1
        break
    if x==0:
        return "true"
    else:
        return "flase"
#---------------------------------------------------
r=int(input("enter the no "))
if(pal(str(r)))and prime(r)=="true":
    print("pal prime")
else:
    print("not pal prime")
     
    
        
