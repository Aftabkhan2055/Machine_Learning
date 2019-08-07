name=input("enetr your name")
address=input("enter your adress")
choice=input("enter your choice laptop or desktop")
rate=int(input("enetr your amoount"))
if choice=="l":
    if  rate>=0 and rate<25000:
        discount=rate*0/100
        netamt=rate-discount
    elif rate>=25001 and rate<57000:
        discount=rate*5.0/100
        netamt=rate-discount
    elif rate>=57001 and rate<100000:
        discount=rate*7.5/100
        netamt=rate-discount
    elif rate>100000:
        discount=rate*10.0/100
        netamt=rate-discount
elif choice=="d":
    if rate>=0 and rate<25000:
        discount=rate*5.0/100
        netamt=rate-discount
    elif rate>=25001 and rate<57000:
        discount=rate*100/7.6
        netamt=rate-discount
    elif rate>=57001 and rate<100000:
        discount=rate*100/10.0
        netamt=rate-discount
    elif rate>100000:
        discount=rate*100/15.0
        netamt=rate-discount

print("dicount on laptop and desktop",discount)
print("net amount  u have to pay",netamt)
        
    
    
    
