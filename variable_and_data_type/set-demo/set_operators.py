set1 = {'apple', 'banana', 'cherry'}

# get length of set
print(len(set1))

# clear set

set1.clear()
print(set1)

del set1
# print(set1)  # error

set1 = {'apple', 'banana', 'cherry'}
set2 = {1, 2, 3}
set3 = set1.union(set2)  # return new set
print(set3)

set1.update(set2)  # insert set2 items into set1
print(set1)

# constructor
set4 = set(('apple', 'banana', 'cherry')) # note the double round-brackets
print(set4)

# different between 2 sets
set5 = {'apple', 'dragon fruit', 'mango'}
set6 = set5.difference(set1)
print(set6)

# different update
print(set5)
set5.difference_update(set1)
print(set5)

set5.discard('mango')
print(set5)

# intersection between 2 sets
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.intersection(y)
print(z)
x.intersection_update(y)
print(x)

# isdisjoint
z = x.isdisjoint(y)
print(z)

# check subset, superset
set7 = {'a', 'b', 'c'}
set8 = {'f', 'e', 'd', 'c', 'b', 'a'}

print(set7.issubset(set8))
print(set8.issuperset(set7))

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

# symmetric difference
z = x.symmetric_difference(y)
print(z)

# symmetric difference update
x.symmetric_difference_update(y)
print(x)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

# union
z = x.union(y)
print(z)

