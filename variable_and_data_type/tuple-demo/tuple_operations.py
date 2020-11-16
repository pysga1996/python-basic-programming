tuple1 = ('apple', 'banana', 'cherry')
del tuple1
# print(tuple1)  # error

# join 2 tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple constructor
tuple4 = tuple(('apple', 'banana', 'cherry', 'banana'))
print(tuple4)

# count tuple elements
print(tuple4.count('banana'))

# get position of item
print(tuple4.index('banana'))

