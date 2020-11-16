import os

# delete file if exist
file_path = 'my_file.txt'
if os.path.isfile(file_path):
    os.remove(file_path)
else:
    print('The file does not exist')

# delete directory
dir_path = 'my_dir'
if os.path.isdir(dir_path):
    os.rmdir(dir_path)
else:
    print('The directory does not exist')

