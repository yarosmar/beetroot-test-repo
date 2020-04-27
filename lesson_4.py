# Task_1

import random

testList = []

for i in range(10):
    testList.append(random.randrange(1, 11))

print(testList)

n = 1
largest = max(testList)

while n < len(testList):
    if testList[n] > largest:
        largest = testList[n]
    n = n+1

print(largest)



#Task_2

import random

testList1 = [] #[] - провірка на наявність елементів в списку
testList2 = []

for i in range(10):
    testList1.append(random.randrange(1, 11))
    testList2.append(random.randrange(1, 11))

myList = testList1 + testList2

print(myList)
print(len(myList))
print(set(myList)) #функція set для оприділення унікальності списку,
                   #тим самим видаляэ дублікати



#Task_3

for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
    
