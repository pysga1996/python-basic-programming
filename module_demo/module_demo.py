import module1 as mx
import platform
from module2 import array as my_array

mx.greeting('Vu Tat Thanh')

a = mx.person1['age']
print(a)
print(type(mx.person1))

x = platform.system()
print(x)

# List all the defined names belonging to the platform module
y = dir(platform)
print(y)

for i in my_array:
    print(i)



