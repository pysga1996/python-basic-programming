import re

txt = 'The rain in Spain'
x = re.search('\s', txt)

print('The first white-space character is located in position:', x.start())

x = re.search("Portugal", txt)
print(x)
