from func_declare import *
# normal function
hello_func()

# argument
intro_func('Thanh')

# multiple arguments
intro_func_2('Thanh', 'Tat', 'Vu')

# unknown number of arguments
fruit_intro_func('banana', 'orange', 'watermelon')

# key word arguments
child_intro_func(child1='Emil', child2='Tobias', child3='Linus')

# arbitrary keyword arguments
child_intro_func_2(fname="Tobias", lname='Refsnes')

# default value of argument
country_intro_func()

# list of arguments:
fruits = {'apple', 'banana', 'cherry'}
fruit_list_func(fruits)

# return value:
x = multiply_by_5_func(2)
print(x)

# empty body
empty_func()

# recursion
y = factorial_func(5)
print(y)
