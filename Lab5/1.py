import re
def func1(text):
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(func1('aaaa'))                         
print(func1('abb'))
print(func1('bb'))