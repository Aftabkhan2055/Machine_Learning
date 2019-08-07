import math
n=int(input("enter the no"))
total=0
for i in range(1,n+1):
    total=total+math.factorial(i)
    print(total,end=" ")
    
