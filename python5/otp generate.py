#write a program to print six digit otp number
import random
ans=" "
for i in range (1,7):
    ans=ans+str(random.randint(0,9))
print(ans)
    
