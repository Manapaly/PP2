# Write a Python program to test whether a given path exists or not. 
# If the path exist find the filename and directory portion of the given path.
import os
def func1(path):
    print("Test a path exists or not:")
    check = os.access(path, os.F_OK)
    if check==True:
        print('Да такой путь существует')
        print("\nFile name of the path:")
        print(os.path.basename(path))
        print("\nDir name of the path:")
        print(os.path.dirname(path))
    else:
        print('Такого пути нет')
    print('-'*55)
        
func1('D:\pp\pp2\Lab6\Dir-and-files\check1_for1')
func1('D:\pp\pp2\Lab6\Dir-and-files\check1_for2')