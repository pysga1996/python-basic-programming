import os

# Create a file, returns an error if the file exist
# f1 = open('my_file.txt', 'x')

# Create a new file if it does not exist:
f2 = open('my_file.txt', 'w')

# Create a dir
os.mkdir('my_dir', 777)
