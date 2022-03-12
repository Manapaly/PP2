import re

from numpy import False_

def func5(s):
    pattern = r'a.+b$'
    if re.search(pattern, s):
        return True
    else:
        return False

print(func5('aaaaab'))
print(func5('aaaaa'))
print(func5('abbbbbb'))
print(func5('abababab'))
print(func5('acccb'))
print(func5('bbbbAA'))
