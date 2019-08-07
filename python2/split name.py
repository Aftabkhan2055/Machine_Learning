x=input("enter the name comma seprated format")
for i in range(0,len(x)):
    y=x.split(",")
    y.sort()
for r in y:
    print(r)
