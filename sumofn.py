n=int(input("enter the any number"))
if n<0:
    print("the number is positive")
else:
    sum=0
    while n>0:
        sum+=n
        n-=1
    print("the sum of natural no is",sum)