km=int(input("enter the kilometer"))
if km>=1 and km<50:
    bill=(km*5.5)
elif km>=50 and km<100:
    bill=(275+(km-50)*10)
elif km>=100:
    bill=(275+500+(km-100)*15)
total =bill
print("charges",total+50)


      
