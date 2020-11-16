tuple1 = ('apple', 'banana', 'cherry')
print(tuple1)
print(tuple1[1])
print(tuple1[-1])
tuple2 = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(tuple2[2:5])
print(tuple2[-4:-1])

# change tuple value
x = tuple(tuple1)
print(x)
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

# create tuple with 1 item
tuple3 = ('dragon fruit',)
print(type(tuple3))
tuple4 = ('dragon fruit')  # not a tuple
print(type(tuple4))
