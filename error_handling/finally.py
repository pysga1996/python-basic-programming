import os

file_path = 'demo_file.txt'
f = open(file_path, 'r')
try:
    print(os.path.isfile(file_path))
    f.write('Lorum Ipsum')
except IOError:
    print('Something went wrong when writing to the file')
finally:
    f.close()

try:
    print(x)
except Exception as ex:
    print(ex.__cause__)
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
