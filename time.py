
class time:
    def __init__(self, h, m):
        self.__hours = h
        self.__minutes = m

    def __add__(self, other):
        total = self.__minutes + other.__minutes
        hours = self.__hours + other.__hours + total // 60
        minutes = total % 60
        return time(hours, minutes)

    def display(self):
        print("Time:", self.__hours, "hours", self.__minutes, "minutes")


h1 = int(input("Enter hours: "))
m1 = int(input("Enter minutes: "))
h2 = int(input("Enter hours: "))
m2 = int(input("Enter minutes: "))

t1 = time(h1, m1)
t2 = time(h2, m2)

t3 = t1 + t2

print("Sum of two times:")
t3.display()
