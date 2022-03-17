# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os

file = 'D:\pp\pp2\Lab6\Dir-and-files\check_for8'
if os.access(file, os.F_OK)==True:
    os.remove(file)
else:
    print('Такого файла нет')