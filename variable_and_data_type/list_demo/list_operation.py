list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
print(list2)
list3 = list(list1)
print(list3)
list4 = list('T am a list')
print(list4)

# join 2 lists
list5 = list1 + list4
print(list5)

for x in list4:
    list1.append(x)
print(list1)

list2.extend(list4)
print(list2)

# list constructor
list7 = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(list7)

print(list4.count(' '))

# reverse list
list7.reverse()
print(list7)

# sort list
cars = ['Ford', 'BMW', 'Volvo', 'Kia', 'Hyundai', 'Toyota', 'Honda', 'Mazda', 'Mitsubishi', 'Nissan']
cars.sort()
print(cars)
cars.sort(key=lambda e: len(e), reverse=True)
print(cars)


