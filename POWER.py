n=int(input("Enter any pos number: "))
e=int(input("Enter any value of exponent: "))
p=1
for i in range(1,e+1):
    p=p*n
print("the power of ",n,"^",e,"is",p)
