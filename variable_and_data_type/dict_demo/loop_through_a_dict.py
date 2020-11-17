from access_items import dict1
for x in dict1.keys(): # or can use dict1 instead
    print(x + ': ' + str(dict1[x]), end=', ')
print()
for x in dict1.values():
    print(x, end=',')
print()
if 'model' in dict1:
    print('Yes, "model" is one of the keys in the dict1 dictionary')

print(len(dict1))
