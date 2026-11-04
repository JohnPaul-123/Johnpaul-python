def perfectSquare(l,r):
    for i in range(l,r+1):
        if(i**(.5)==int(i**(.5))):
            print(i,end=" ")
l=2
r=24
perfectSquare(l,r)