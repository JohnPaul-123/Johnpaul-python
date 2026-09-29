a=(int(input("Enter the first number: ")))
b=(int(input("Enter the second number: ")))
print(" a addition")
print(" b subtraction")
print(" c multiplication")
print(" d division")
c=(input("Enter your choice: "))
if(c=="a"):
    print(a+b)
elif(c=="b"):
    print(a-b)
elif(c=="c"):
    print(a*b)
elif(c=="d"):
    print(a/b)
else:
    print("Invalid Choice")