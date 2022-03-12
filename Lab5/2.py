import re

def func2(s):
    pattern = r'ab{2,3}'
    if re.search(pattern, s):
        return True
    else:
        return False

print(func2('abbb'))
print(func2('aaaaa'))
print(func2('abab'))