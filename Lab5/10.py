#camel to snake
import re
s = input()
pattern = r'(.)([A-Z])'
x = re.sub(pattern, r'\1_\2', s).lower()
print(x)