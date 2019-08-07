def pal(s):
    ans=""
    for i in range (len(s)-1,-1,-1):
        ans=ans+s[i]
    if ans==s:
        print(s,end=" ")
#--------------------------------------------------
p=input("enter the string")
y=p.split(" ")
for r in y:
    pal(r)
    

