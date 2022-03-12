import re

def func4(s):
    pattern = r'[A-Z][a-z]{2,}'
    if re.search(pattern, s):
        return True
    else:
        return False

print(func4('AAAAAb'))
print(func4('aaaaaBBBBB'))
print(func4('AAAAAbbbb'))
print(func4('AAAAAA'))
print(func4('bbbAbbb'))
