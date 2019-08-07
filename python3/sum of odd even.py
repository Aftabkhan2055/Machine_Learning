x=int(input("enter the string"))
even=0
odd=0
for i in range(1,x+1):
    if   i%2==0:
        even=even+i
    else:
        i%2!=0
        odd=odd+i
print("sum of even",even)
print("sum of odd",odd)
    
