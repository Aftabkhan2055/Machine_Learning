x=input("enter the string")
ans=" "
for i in range (0,len(x)):
    if i%2==0:
        ans=ans+x[i].upper()
    else:
        ans=ans+x[i].lower()
        print(ans)

        
