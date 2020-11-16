import re

txt = 'The rain in Spain'
x = re.split('\s', txt)
print(x)

# Split the string only at the first occurrence:
x = re.split('\s', txt, maxsplit=1)
print(x)