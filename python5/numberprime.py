def pal(s):
    rev=""
    for i in range (len(s)-1,-1,-1):
        rev=rev+s[i]
    if rev==s:
        return "true"
    else:
        return "false"
#----------------------------------
n=int(input("enter the no"))
print(pal(str(n)))
     
