import constants


fruits = ["apple", "banana", "cherry"]


def changeValue(number):
    print(number)
    number += 5
    print(number)


def pushToArray(array, value):
    array.append(value)


print('Hello World!')
x = 5
for i in fruits:
    print(i)
changeValue(5)
pushToArray(fruits, "orange")
for i in fruits:
    print(i)
print('x = {value}'.format(value=x))

