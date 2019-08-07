x=(input("enter the string and find vowel"))
count=0
for i in range (0,len(x)):
    if x[i]=="A" or x[i]=="E" or x[i]=="I" or x[i]=="O" or x[i]=="U" or x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u":
        count=count+1
        print(x[i])
print("total vowel is",count,)
