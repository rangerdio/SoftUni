import os
try:
    os.remove('../3/my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')
