def find_lcm(a,b):
    if a>b:
        greatest=a
    else:
        greatest=b

    while(True):
        if greatest%a==0 and greatest%b==0:
            lcm=greatest
            break
        greatest+=1
    return lcm
a=int(input("enter the value of first number"))
b=int(input("enter the value of second number"))
print("the LCM is",find_lcm(a,b))