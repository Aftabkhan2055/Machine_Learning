
a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
#while(n-2):
for i in range (1,n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-2
#1. Take the first two numbers of the series and the number of terms to be printed from the user.
#2. Print the first two numbers.
#3. Use a while loop to find the sum of the first two numbers and then proceed the fibonacci series.
#4. Print the fibonacci series till n-2 is greater than 0.
#5. Exit.
