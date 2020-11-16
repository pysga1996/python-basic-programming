import re

txt = 'The rain in Spain'
x = re.search('ai', txt)
print(x)  # this will print an object

# Print the position (start- and end-position) of the first match occurrence
print(x.span())

# Print the string passed into the function
print(x.string)

# The regular expression looks for any words that starts with an upper case "S"
print(x.group())
