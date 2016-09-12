import random

n = int(input())

mylist = []

for i in range(0,n):
    mylist.append(random.randint(0,100000))

print(n)

for i in mylist:
    print(i, end = " ")
