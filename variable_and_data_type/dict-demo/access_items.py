dict1 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
if __name__ == '__main__':
    print(dict1)
    x = dict1['model']
    print(x)
    x = dict1.get('model')
    print(x)
    dict1['year'] = 2018
    print(dict1)

