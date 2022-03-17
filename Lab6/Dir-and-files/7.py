# Write a Python program to copy the contents of a file to another file
first_file = open('D:\pp\pp2\Lab6\Dir-and-files\check_for7_1.txt', "r")
texts = first_file.readlines()
first_file.close()

second_file = open('D:\pp\pp2\Lab6\Dir-and-files\check_for7_2.txt', "w")
for s in texts:
    second_file.write(s)
second_file.close()