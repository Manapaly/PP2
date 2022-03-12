import re

def func3(s):
    pattern = r'[a-z]+_[a-z]'
    if re.search(pattern, s):
        return True
    else:
        return False

print(func3('afddsa_asfsa'))
print(func3('fdsfA_adf'))
print(func3('asdAsa_asda'))
print(func3('asdsaf_'))
print(func3('_asdsaf'))
print(func3('asdsaf'))