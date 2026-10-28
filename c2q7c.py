#7c
list1=[1,2,4,3,8,7]
list2=[1,2,4,3,5,7]
print("THe firt list is :"+str(list1))
print("The second list is :"+str(list2))
print("The values occur in both lists:")
for i in list1:
    if i in list1 and i in list2:
        print(i)