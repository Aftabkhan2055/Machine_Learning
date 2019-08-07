import math
a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
d=b**2-4*a*c
if d<0:
    print(" root are imaginary",d)
elif  d==0:
    root=math.sqrt(d)/2*a
    print("root are equal",root)
else:
    root1=-b+math.sqrt(d)/2*a
    root2=-b-math.sqrt(d)/2*a
    print("seprateroot",root1)
    print("seprateroort",root2)
    
    
