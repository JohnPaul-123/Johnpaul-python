n = int(input("Enter the Number:"))
rev=0
temp=n
while temp>0:
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10
print("Reverse of this given number is ",rev)
if rev==n:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")