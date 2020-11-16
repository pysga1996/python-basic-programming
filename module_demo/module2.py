def count_number_of_elements(plist):
    if isinstance(plist, (list, tuple, set)):
        return len(plist)
    else:
        raise Exception('Argument is not an iterable object')


array = ['red', 'green', 'blue', 'yellow']
