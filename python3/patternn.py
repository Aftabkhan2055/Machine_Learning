for i in range (1,6):
    for j in range( 1,(6-i)+1):
        print("*",end=" ")
    for k in range(1,(2*i-2)+1):
        print(" ",end=" ")
    for r in range(1,(6-i)+1):
        print ("*",end=" ")
    print()   
