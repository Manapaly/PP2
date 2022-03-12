import re
# s = input()
x = re.findall('[A-Z][a-z]*', 'MyNameIsErnat')
print(*x)