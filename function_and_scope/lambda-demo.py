x = lambda a: a + 10
print(x(5))

y = lambda a, b: a * b
print(y(5, 6))

z = lambda a, b, c: a + b + c
print(z(5, 6, 2))


def my_func(n):
    return lambda a: a * n


my_doubler = my_func(2)
my_tripler = my_func(3)
print(my_doubler(11))
print(my_tripler(11))


