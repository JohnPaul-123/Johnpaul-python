n=int(input("Enter any number"))
x,y=0,1
count=0
if n<=0:
    print("enter a positive integer")
elif n==1:
    print("1st Fibonacci number")
    print(x)
else:
    print("Fibonacci numbers are : ")
    while count<n:
        print(x)
        z=x+y
        x=y
        y=z
        count=count+1
