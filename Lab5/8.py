import re
s = input()
pattern = r'[A-Z][a-z]+'
l = re.findall(pattern,s)
print(*l)

