#7b
list1=[1,2,4,3,8]
list2=[1,2,4,3,8]
print("The first list is :"+str(list1))
print("The second list is :"+str(list2))
sum1=0
sum2=0
for x in range(0,len(list1)):
    sum1=sum1+list1[x]
print("Sum of all the numbers in the list1 is :",sum1)
for x in range(0,len(list2)):
    sum2=sum2+list2[x]
print("Sum of all the numbers in the list2 is :",sum2)
if sum1==sum2:
    print("List sums are same values")
else:
    print("List sums are different")