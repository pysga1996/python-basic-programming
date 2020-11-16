def hello_func():
    print('Hello from a function')


def intro_func(name):
    print('My name is ' + name)


def intro_func_2(fname, mname, lname):
    print('My full name is ' + lname + ' ' + mname + ' ' + fname)


def fruit_intro_func(*args):
    print("I d'like to eat ", end='')
    print(args, sep=', ')


def child_intro_func(child3, child2, child1):
    print('The youngest child is ' + child3)


def child_intro_func_2(**kid):
    print("His last name is " + kid["lname"])


def country_intro_func(country='Vietnam'):
    print('I am from ' + country)


def fruit_list_func(p_list):
    print('p_list is an instance of ' + str(type(p_list)))
    if isinstance(p_list, (list, tuple, set)):
        for x in p_list:
            print(x)


def multiply_by_5_func(x):
    return 5 * x


def empty_func():
    pass


def factorial_func(k):
    if k > 0:
        return k * factorial_func(k - 1)
    else:
        return 1




