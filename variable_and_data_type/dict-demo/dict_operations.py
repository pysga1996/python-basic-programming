from access_items import dict1

print(dict1)

# copy dict
dict2 = dict1.copy()
print(dict2)

# nested dict
my_family = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}

# constructor
dict3 = dict(brand='Ford', model='Mustang', year=1964)
