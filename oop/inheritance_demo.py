from class_declarre import *

x = Person('John', 'Doe')
x.print_name()

y = Student('Mike', 'Olsen', 2010)
y.print_name()

print(isinstance(y, Person))

z = Student('Mike', 'Olsen', 2019)
z.welcome()

print(isinstance(z, Person))

