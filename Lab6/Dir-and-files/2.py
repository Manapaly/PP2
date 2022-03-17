# Write a Python program to check for access to a specified path. Test the existence, 
# readability, writability and executability of the specified path
# os.F_OK - объект существует, 
# os.R_OK - доступен на чтение, 
# os.W_OK - доступен на запись, 
# os.X_OK - доступен на исполнение.
import os
print('Существование:', os.access('D:\pp\pp2\Lab6\Dir-and-files\check1_for2', os.F_OK)) # False так как у меня нет файла check1_for2
print('Чтение доступно:', os.access('D:\pp\pp2\Lab6\Dir-and-files\check1_for1', os.R_OK))
print('Запись доступна:', os.access(__file__, os.W_OK))
print('Доступен на исполнение:', os.access(__file__, os.X_OK))