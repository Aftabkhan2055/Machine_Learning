def demo(n):
    u=n
    l=len(u)
    t=""
    for i in range (0,l-1):
        t=t+s[i]
    p=s[len(s)-1]+t
    return p
#-------------------------------------------------------

s=input("enter the string")
for i in range (0,len(s)):
    x=demo(s)
    s=x
    print(s)
