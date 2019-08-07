def prime(n):
    x=0
    for i in range (2,n+1):
        if n%i==0:
            x=1
        break
    if x==0:
        return n
    else:
        return 0
    
    
#--------------------------------------------
total=0
for i in range(1,101):
    total=total+prime(i)
    print(total)
    
    
        
