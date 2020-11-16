# local scope
def my_func():
    x = 300
    print(x)

    def my_inner_func():
        print(x)

    my_inner_func()


my_func()
