x = 300


def my_func():
    x = 200
    print(x)


my_func()

print(x)
# change global var value inside a function


def my_func_2():
    global x
    x = 500


my_func_2()
print(x)
