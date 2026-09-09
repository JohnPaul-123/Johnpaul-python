current=int(input("Enter the current year: "))
final=int(input("Enter the final year: "))
for i in range(current,final):
    if i%4==0:
        print(i)