name=input("enter your name")
charge=int(input("enter the charges"))
if charge>=2000 and charge<5000:
    discount=charge*5/100
    netamt=charge-discount
    print("discount",discount)
    print("net amount",netamt)
elif charge>=5000 and charge<10000:
    discount=charge*8/100
    netamt=charge-discount
    print("discount",discount)
    print("net amount",netamt)
elif charge>=10000 and charge<15000:
    discount=charge*10/100
    netamt=charge-discount
    print("discount",discount)
    print("net amount",netamt)
elif charge>=15000 and charge<20000:
    discount=charge*12/100
    netamt=charge-discount
    print("discount",discount)
    print("net amount",netamt)
else:
    print("wrong choice")
    
    
    
    
    
    
