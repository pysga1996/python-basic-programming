from access_items import dict1

print(dict1)

dict1["color"] = "red"
print(dict1)

x = dict1.setdefault('gear_type', 'automatic')
y = dict1.setdefault('model', 'Bronco')
print(dict1)

dict1.update({'tier': 'E', 'drive_type': '2WD'})
print(dict1)

dict1.pop('model')
print(dict1)

dict1.popitem()
print(dict1)

del dict1
# print(dict1)  # error
