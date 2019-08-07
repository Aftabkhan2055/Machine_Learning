s=input("enter the string")
s=s.upper()
ans=''
for i in range (len(s)-1,-1,-1):
    ans=ans+s[i]
if ans==s:
    print(" given string is palindrome")

else:
    print(" given string is not palindrome")                                                                                                                                                                                                           

        
