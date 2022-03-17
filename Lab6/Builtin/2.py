#2 Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def func2(s):
    count1 = 0
    count2 = 0
    for i in s:
        if i.islower():
            count1+=1
        elif i.isupper():
            count2+=1
    print(f'The number of lower case letters is {count1}')
    print(f'The number of upper case letters is {count2}')
func2('Abcerf')
# func2('aaaaaaaaa')