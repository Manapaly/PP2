# Write a Python program to count the number of lines in a text file.

def file_lengthy(fname):
    i = 0
    with open(fname) as f:
        for line in f:
            i += 1
        return i
print("Number of lines in the file: ",file_lengthy("check-for4.txt"))