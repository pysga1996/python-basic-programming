fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# loop through a string
for x in 'banana':
    print(x)

# break statement
for x in fruits:
    print(x)
    if x == 'banana':
        break

# continue statement
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# else statement
for x in fruits:
    print(x)
else:
    print('Finally finished!')

# nested loop
colors = ['red', 'big', 'tasty']
for y in colors:
    for x in fruits:
        print(y, x)

# empty loop
for x in [1, 2, 3]:
    pass

for x in range(6):
    print(x)

# range() with start param
for x in range(2, 5):
    print(x)

# range() with step param
for x in range(3, 33, 3):
    print(x)

