class Person:
    pass


a = Person()
b = Person()
c = a

print(a is b)
print(c is a)
print(b is not c)

