import re

txt = 'The rain in Spain'
x = re.sub('\s', '9', txt)
print(x)

# Control the number of replacements by specifying the count parameter:
x = re.sub('\s', '9', txt, count=2)
print(x)
