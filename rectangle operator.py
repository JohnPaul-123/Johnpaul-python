
class Rectangle:
    def __init__(self, l, b):
        self.__length = l
        self.__breadth = b

    def area(self):
        return self.__length * self.__breadth

    def __lt__(self, other):
        return self.area() < other.area()


l1 = int(input("Enter length of first rectangle: "))
b1 = int(input("Enter breadth of first rectangle: "))

l2 = int(input("Enter length of second rectangle: "))
b2 = int(input("Enter breadth of second rectangle: "))

r1 = Rectangle(l1, b1)
r2 = Rectangle(l2, b2)

if r1 < r2:
    print("First rectangle has smaller area")
else:
    print("First rectangle does not have smaller area")
